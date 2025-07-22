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

    def __init__(self, num_heads, query_dim, key_dim, value_dim, dropout_p):
        super().__init__()
        self.softmax_q = torch.nn.Softmax(dim=(- 1))
        self.softmax_k = torch.nn.Softmax(dim=(- 2))
        self.softmax_v = torch.nn.Softmax(dim=(- 2))
        self.dropout_q = torch.nn.Dropout(dropout_p)
        self.dropout_k = torch.nn.Dropout(dropout_p)
        self.dropout_v = torch.nn.Dropout(dropout_p)
        self.linear_q = torch.nn.Linear(query_dim, (num_heads * key_dim))
        self.linear_k = torch.nn.Linear(key_dim, (num_heads * key_dim))
        self.linear_v = torch.nn.Linear(value_dim, (num_heads * key_dim))
        self.linear_output = torch.nn.Linear((num_heads * key_dim), value_dim)

    def forward(self, q, k, v):
        q = self.linear_q(q)
        k = self.linear_k(k)
        v = self.linear_v(v)
        q = self.softmax_q(q).reshape(q.shape[0], (- 1), q.shape[(- 1)])
        k = self.softmax_k(k).reshape(k.shape[0], (- 1), k.shape[(- 1)])
        v = self.softmax_v(v).reshape(v.shape[0], (- 1), v.shape[(- 1)])
        q = self.dropout_q(q)
        k = self.dropout_k(k)
        v = self.dropout_v(v)
        output = q.matmul(k.transpose((- 2), (- 1))).matmul(v)
        output = output.reshape(output.shape[0], q.shape[1], (- 1))
        output = self.linear_output(output)
        return output



num_heads = 1
query_dim = 1
key_dim = 1
value_dim = 1
dropout_p = 1

func = Model(num_heads, query_dim, key_dim, value_dim, dropout_p).to('cuda')



q = torch.randn(1, 16, 32)



k = torch.randn(1, 48, 32)



v = torch.randn(1, 48, 96)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x32 and 1x1)

jit:
Failed running call_module L__self___linear_q(*(FakeTensor(..., device='cuda:0', size=(1, 16, 32)),), **{}):
a and b must have same reduction dim, but got [16, 32] X [1, 1].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''