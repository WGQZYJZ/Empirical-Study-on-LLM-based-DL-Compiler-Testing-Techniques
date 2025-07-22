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
        self.dense = torch.nn.Linear(32, 32)

    def forward(self, q, v, k, scale_factor, dropout_p):
        q = self.dense(q)
        v = self.dense(v)
        k = self.dense(k)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 7, 1, 128)



v = torch.randn(8, 1, 2, 64)



k = torch.randn(7, 8, 3, 64)

scale_factor = 1
dropout_p = 1

test_inputs = [q, v, k, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (7x128 and 32x32)

jit:
Failed running call_module L__self___dense(*(FakeTensor(..., device='cuda:0', size=(1, 7, 1, 128)),), **{}):
a and b must have same reduction dim, but got [7, 128] X [32, 32].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''