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

    def __init__(self, hidden_size, num_heads, dropout_p):
        super().__init__()
        self.qkv_proj = torch.nn.Linear(hidden_size, (num_heads * 3))
        self.dropout_p = dropout_p

    def forward(self, x1, x2=None):
        if (x2 is None):
            x2 = x1
        qkv = self.qkv_proj(x1)
        (q, k, v) = torch.chunk(qkv, chunks=3, dim=(- 1))
        scale_factor = (hidden_size ** (- 0.5))
        inv_scale_factor = (1 / scale_factor)
        q = q.matmul(k.transpose((- 2), (- 1)))
        q = q.div(inv_scale_factor)
        softmax_q = q.softmax(dim=(- 1))
        dropout_q = torch.nn.functional.dropout(softmax_q, p=self.dropout_p)
        output = dropout_q.matmul(v)
        return output



hidden_size = 1
num_heads = 1
dropout_p = 1

func = Model(hidden_size, num_heads, dropout_p).to('cuda')



x1 = torch.randn(4, 16, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x32 and 1x3)

jit:
Failed running call_module L__self___qkv_proj(*(FakeTensor(..., device='cuda:0', size=(4, 16, 32)),), **{}):
a and b must have same reduction dim, but got [64, 32] X [1, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''