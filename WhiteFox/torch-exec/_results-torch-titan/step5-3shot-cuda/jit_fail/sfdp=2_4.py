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

    def __init__(self, n_head, d_qkv, dropout_p):
        super().__init__()
        self.query = torch.nn.Linear(d_qkv, d_qkv)
        self.key = torch.nn.Linear(d_qkv, d_qkv)
        self.value = torch.nn.Linear(d_qkv, d_qkv)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        q = self.query(query)
        k = self.key(key)
        v = self.value(value)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = (1.0 / math.sqrt(d_qkv))
        scaled_qk = (qk * inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output



n_head = 1
d_qkv = 1
dropout_p = 1
func = Model(n_head, d_qkv, dropout_p).to('cuda')

query = 1
key = 1
value = 1

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___query(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''