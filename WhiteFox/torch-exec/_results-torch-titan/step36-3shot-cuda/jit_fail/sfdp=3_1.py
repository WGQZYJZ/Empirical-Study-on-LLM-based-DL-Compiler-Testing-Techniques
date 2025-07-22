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
        self.q = torch.nn.Linear(20, 20, bias=True)
        self.k = torch.nn.Linear(20, 20, bias=True)

    def compute_attention(self, query, key, value, scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

    def forward(self, x1, x2):
        q = self.q(x1)
        k = self.k(x2)
        output = self.compute_attention(query=q, key=k, value=v, scale_factor=f, dropout_p=p)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 20, 10)



x2 = torch.randn(1, 20, 5)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x10 and 20x20)

jit:
Failed running call_module L__self___q(*(FakeTensor(..., device='cuda:0', size=(1, 20, 10)),), **{}):
a and b must have same reduction dim, but got [20, 10] X [20, 20].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''