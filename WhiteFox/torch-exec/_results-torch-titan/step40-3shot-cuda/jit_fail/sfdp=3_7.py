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



class MultiHeadAttention(nn.Module):

    def __init__(self, d_k, d_v, h, dropout_p=0.1):
        super().__init__()
        self.d_k = d_k
        self.d_v = d_v
        self.h = h
        self.dropout_p = dropout_p
        self.q_linear = nn.Linear(d_model, (h * d_k))
        self.v_linear = nn.Linear(d_model, (h * d_v))
        self.k_linear = nn.Linear(d_model, (h * d_k))
        self.dropout = nn.Dropout(dropout_p)
        self.out = nn.Linear((h * d_v), d_model)

    def forward(self, query, key, value):
        bs = query.size(0)
        k = self.k_linear(query).view(bs, (- 1), self.h, self.d_k)
        q = self.q_linear(query).view(bs, (- 1), self.h, self.d_k)
        v = self.v_linear(query).view(bs, (- 1), self.h, self.d_v)
        k = k.transpose(1, 2)
        q = q.transpose(1, 2)
        v = v.transpose(1, 2)
        scores = attention(q, k, v, self.d_k, self.d_v, self.dropout_p)
        concat = scores.transpose(1, 2).contiguous().view(bs, (- 1), (self.d_v * self.h))
        output = torch.tanh(self.out(concat))
        return output




d_k = d_v = 16


d_k = d_v = 16


h = 2

func = MultiHeadAttention(d_k, d_v, h).to('cuda')

query = 1
key = 1
value = 1

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'size'

jit:
'int' object has no attribute 'size'

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''