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

    def __init__(self, d_query, d_key, d_value, d_out, n_heads, scale_factor, drop_p):
        super().__init__()
        self.dropout = torch.nn.Dropout(drop_p)
        self.n_heads = n_heads
        self.head_dim = (d_out // n_heads)
        self.wq = torch.nn.Parameter(torch.zeros(size=(d_query, d_out)))
        self.wk = torch.nn.Parameter(torch.zeros(size=(d_key, d_out)))
        self.wv = torch.nn.Parameter(torch.zeros(size=(d_value, d_out)))
        torch.nn.init.xavier_normal_(self.wq)
        torch.nn.init.xavier_normal_(self.wk)
        torch.nn.init.xavier_normal_(self.wv)
        self.scale_factor = scale_factor

    def forward(self, query, key, value):
        q = torch.matmul(query, self.wq)
        k = torch.matmul(key, self.wk)
        v = torch.matmul(value, self.wv)
        q = q.reshape((q.shape[:(- 1)] + (self.n_heads, self.head_dim)))
        k = k.reshape((k.shape[:(- 1)] + (self.n_heads, self.head_dim)))
        v = v.reshape((v.shape[:(- 1)] + (self.n_heads, self.head_dim)))
        q = q.permute((0, 2, 1, 3))
        k = k.permute((0, 2, 1, 3))
        v = v.permute((0, 2, 1, 3))
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = torch.empty_like(qk).fill_((1 / self.scale_factor))
        qk = (qk * inv_scale_factor)
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        attended = torch.matmul(dropout_qk, v)
        attended = attended.permute((0, 2, 1, 3))
        attended = attended.reshape((attended.shape[:(- 2)] + ((self.n_heads * self.head_dim),)))
        return attended



d_query = 1
d_key = 1
d_value = 1
d_out = 1
n_heads = 1
scale_factor = 1
drop_p = 1

func = Model(d_query, d_key, d_value, d_out, n_heads, scale_factor, drop_p).to('cuda')



query = torch.randn(1, 10, 26)



key = torch.randn(1, 8, 26)



value = torch.randn(1, 8, 26)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x26 and 1x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x747bb98699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 10, 26)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 1), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [10, 26] X [1, 1].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''