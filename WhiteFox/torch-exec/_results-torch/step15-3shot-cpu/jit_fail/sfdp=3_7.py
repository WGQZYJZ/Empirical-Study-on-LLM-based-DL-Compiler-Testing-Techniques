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

class SelfAttention(torch.nn.Module):

    def __init__(self, query_len: int, key_len: int, value_len: int, dropout_p: float=0.5):
        super().__init__()
        self.scale_factor = torch.tensor(1 / key_len)
        self.dropout_p = dropout_p
        self.W_V = torch.nn.Linear(32, 32)
        self.W_K = torch.nn.Linear(32, 32)
        self.W_Q = torch.nn.Linear(32, 32)
        self.W_O = torch.nn.Linear(32, 32)

    def compute_attention(self, query, key, value):
        q1 = self.W_Q(query)
        k1 = self.W_K(key)
        v1 = self.W_V(value)
        q2 = q1.view(q1.shape[0], 1, q1.shape[1])
        k2 = k1.view(k1.shape[0], k1.shape[1], 1)
        q3 = q2 * k2
        s = q3.mean(dim=2)
        s = s.mul(self.scale_factor)
        s = s.exp()
        s = s.mean(dim=1)
        d2 = 1 - s
        d1 = 1 - torch.nn.functional.dropout(d2, p=self.dropout_p)
        m = v1 * d1.view(d1.size(0), 1, 1)
        o = m.mean(dim=1)
        return self.W_O(o)

    def forward(self, query, key, value):
        query_len = query.shape[-2]
        key_len = key.shape[-2]
        value_len = value.shape[-2]
        attention = self.compute_attention(query, key, value)
        return attention


query_len = 1
key_len = 1
value_len = 1
func = SelfAttention(32, 32, 32).to('cpu')


query = torch.randn(8, 32, 32)

key = torch.randn(8, 64, 32)

value = torch.randn(8, 64, 32)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
shape '[8, 1, 32]' is invalid for input of size 8192

jit:
Failed running call_method view(*(FakeTensor(..., size=(8, 32, 32)), 8, 1, 32), **{}):
shape '[8, 1, 32]' is invalid for input of size 8192

from user code:
   File "<string>", line 45, in forward
  File "<string>", line 28, in compute_attention


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''