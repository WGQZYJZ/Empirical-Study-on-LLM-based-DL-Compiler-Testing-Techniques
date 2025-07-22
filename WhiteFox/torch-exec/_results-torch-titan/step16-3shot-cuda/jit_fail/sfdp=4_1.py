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

    def __init__(self, dim, num_heads):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.to_q = torch.nn.Linear(dim, dim)
        self.to_k = torch.nn.Linear(dim, dim)
        self.to_v = torch.nn.Linear(dim, dim)
        self.to_o = torch.nn.Linear(dim, dim)

    def forward(self, query, key, value, attn_mask):
        q = self.to_q(query)
        k = self.to_k(key)
        v = self.to_v(value)
        q_ = q.reshape(*q.shape[:(- 1)], self.num_heads, (q.shape[(- 1)] // self.num_heads)).transpose((- 3), (- 2))
        k_ = k.reshape(*k.shape[:(- 1)], self.num_heads, (k.shape[(- 1)] // self.num_heads)).transpose((- 3), (- 2))
        v_ = v.reshape(*v.shape[:(- 1)], self.num_heads, (v.shape[(- 1)] // self.num_heads)).transpose((- 3), (- 2))
        qk = ((q_ @ k_.transpose((- 2), (- 1))) / math.sqrt(v_.shape[(- 1)]))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v_)
        output = output.transpose((- 3), (- 2)).reshape(*output.shape[:(- 2)], output.shape[(- 2)], (output.shape[(- 1)] * self.num_heads))
        output = self.to_o(output)
        return output



dim = 1
num_heads = 1

func = Model(dim, num_heads).to('cuda')



x1 = torch.randn(1, 10, 64)



x2 = torch.randn(1, 15, 64)


x2 = torch.randn(1, 15, 64)


x1 = torch.randn(1, 10, 64)


x1 = torch.randn(1, 10, 64)



x1 = torch.randn(1, 10, 64)


attn_mask = torch.randint(0, 2, size=(x1.shape[0], x1.shape[1], x2.shape[1])).type_as(x1)

query = 1

test_inputs = [x1, x2, attn_mask, query]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x64 and 1x1)

jit:
Failed running call_module L__self___to_q(*(FakeTensor(..., device='cuda:0', size=(1, 10, 64)),), **{}):
a and b must have same reduction dim, but got [10, 64] X [1, 1].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''