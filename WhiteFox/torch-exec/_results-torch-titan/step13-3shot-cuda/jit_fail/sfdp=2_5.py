import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.dropout_p = 0.5
        self.inv_scale_factor = (1 / (self.dropout_p * 9))
        self.linear_0 = torch.nn.Linear(128, 128, False)
        self.linear_1 = torch.nn.Linear(128, 128, False)
        self.linear_2 = torch.nn.Linear(256, 128, False)
        self.linear_out = torch.nn.Linear(128, 256, False)

    def forward(self, query, key, value, mask):
        r1 = self.linear_0(query)
        r2 = self.linear_1(key)
        r3 = self.linear_2(value)
        qk = torch.matmul(r1, r2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        v1 = dropout_qk.matmul(r3)
        v2 = self.linear_out(v1)
        output = (v2 + mask.matmul(value))
        return output



func = Model().to('cuda')



query = torch.randn(2, 6, 128)



key = torch.randn(1, 50, 128)



value = torch.randn(1, 50, 128)



mask = torch.randn(2, 50, 128)


test_inputs = [query, key, value, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (50x128 and 256x128)

jit:
Failed running call_module L__self___linear_2(*(FakeTensor(..., device='cuda:0', size=(1, 50, 128)),), **{}):
a and b must have same reduction dim, but got [50, 128] X [256, 128].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''