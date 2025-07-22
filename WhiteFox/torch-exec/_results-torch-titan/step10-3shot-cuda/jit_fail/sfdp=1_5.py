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

    def __init__(self, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.q = torch.nn.Sequential(torch.nn.Linear(16, 16), torch.nn.LayerNorm(normalized_shape=16), torch.nn.Linear(16, 16))
        self.k = torch.nn.Sequential(torch.nn.Linear(16, 16), torch.nn.LayerNorm(normalized_shape=16), torch.nn.Linear(16, 16))
        self.v = torch.nn.Sequential(torch.nn.Linear(16, 16), torch.nn.LayerNorm(normalized_shape=16), torch.nn.Linear(16, 16))

    def forward(self, query, key, value, inv_shiftscale_factor, dropout_p):
        q = self.q(query).reshape(((- 1), self.num_heads, 4, 4)).transpose((- 2), (- 3))
        k = self.k(key).reshape(((- 1), self.num_heads, 4, 4)).transpose(1, 2)
        v = self.v(value).reshape(((- 1), self.num_heads, 4, 4)).transpose(1, 2)
        qk = torch.matmul(q, k)
        scaled_qk = qk.div(inv_shiftscale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



num_heads = 1
func = Model(4).to('cuda')



query = torch.randn(16, 32)



key = torch.randn(16, 32)



value = torch.randn(16, 32)



inv_shiftscale_factor = torch.randn(16, 1)

dropout_p = 1

test_inputs = [query, key, value, inv_shiftscale_factor, dropout_p]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x32 and 16x16)

jit:
Failed running call_module L__self___q_0(*(FakeTensor(..., device='cuda:0', size=(16, 32)),), **{}):
a and b must have same reduction dim, but got [16, 32] X [16, 16].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''