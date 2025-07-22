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
        self.heads = 32
        self.seq_len = 8192
        self.dim = 768 // self.heads

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = attn_weight @ value
        return output



func = Model().to('cpu')


query = torch.randn(1, 8, 37, 37, 768)

key = torch.randn(1, 8, 37, 37, 768)

value = torch.randn(1, 8, 37, 37, 768)

attn_mask = torch.randn(1, 1, 37, 37, 37, 37)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (37) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, s0, s1, s10, s11)), FakeTensor(..., size=(1, 1, s8, s1, s10, s11))), **{}):
The size of tensor a (s0) must match the size of tensor b (s8) at non-singleton dimension 2)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''