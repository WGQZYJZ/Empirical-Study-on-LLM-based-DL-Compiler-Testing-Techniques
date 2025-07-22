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
        size = 64
        self.query = torch.nn.Linear(size, size)
        self.key = torch.nn.Linear(size, size)
        self.value = torch.nn.Linear(size, size)

    def forward(self, query, key, value, mask):
        q = self.query(query)
        k = self.key(key)
        v = self.value(value)
        v_shape = v.shape
        v = v.reshape([(- 1), v_shape[1], v_shape[2]])
        size = q.shape
        k = k.reshape([size[0], size[1], size[2], size[3]])
        attn_mask = mask.reshape(*size, 1)
        qk = torch.matmul(q, (k.transpose((- 2), (- 1)) / math.sqrt(size[(- 1)])))
        return torch.matmul(torch.reshape(torch.softmax((qk + attn_mask), dim=(- 2)), v_shape), v)



func = Model().to('cuda')



x1 = torch.randn(12, 64, 8)



x2 = torch.randn(12, 64, 8)



x3 = torch.randn(12, 64, 8)




mask = torch.triu(torch.ones(16, 31, 31), diagonal=0)


test_inputs = [x1, x2, x3, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (768x8 and 64x64)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(12, 64, 8)),), **{}):
a and b must have same reduction dim, but got [768, 8] X [64, 64].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''