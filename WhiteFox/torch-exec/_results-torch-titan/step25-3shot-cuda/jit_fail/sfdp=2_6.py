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
        self.linear1 = torch.nn.Linear(in_features=50, out_features=8, bias=True)
        self.linear2 = torch.nn.Linear(in_features=8, out_features=8, bias=True)
        self.linear3 = torch.nn.Linear(in_features=8, out_features=8, bias=True)
        self.linear4 = torch.nn.Linear(in_features=8, out_features=8, bias=True)
        self.gru1 = torch.nn.GRU(8, 16, 1)

    def forward(self, q, k, v, inv_scale_factor=1.0):
        q1 = self.linear1(q)
        k1 = self.linear2(k)
        v1 = self.linear3(v)
        qk = torch.matmul(q1, k1.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(v1)
        output = output.transpose(0, 1)
        (_, hidden) = self.gru1(output)
        return hidden[0]



func = Model().to('cuda')



q = torch.randn(10, 8)



k = torch.randn(16, 8)



v = torch.randn(32, 8)



p = torch.randn(50)


test_inputs = [q, k, v, p]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x8 and 50x8)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(10, 8)),), **{}):
a and b must have same reduction dim, but got [10, 8] X [50, 8].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''