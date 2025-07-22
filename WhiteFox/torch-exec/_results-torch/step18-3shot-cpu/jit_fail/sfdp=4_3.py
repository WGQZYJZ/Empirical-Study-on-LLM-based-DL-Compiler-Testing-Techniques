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

    def __init__(self, num_heads, hidden_dim, num_positions):
        super().__init__()
        self.wq = torch.nn.Linear(hidden_dim, hidden_dim // num_heads)
        self.wk = torch.nn.Linear(hidden_dim, hidden_dim // num_heads)
        self.wv = torch.nn.Linear(hidden_dim, hidden_dim // num_heads)

    def forward(self, query, key, value, attn_mask):
        q = self.wq(query)
        k = self.wk(key)
        v = self.wv(value)
        q = q.transpose(0, 1)
        k = k.transpose(0, 1)
        v = v.transpose(0, 1)
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output.transpose(0, 1)


num_heads = 1
hidden_dim = 1
num_positions = 1
func = Model(8, 1024, 1024).to('cpu')


query = torch.randn(16, 8, 1024)

key = torch.randn(16, 8, 1024)

value = torch.randn(16, 8, 1024)


attention_mask = torch.zeros((16, 1, 1, 1024), dtype=torch.int64)

test_inputs = [query, key, value, attention_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (1024) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(8, 16, 16)), FakeTensor(..., size=(16, 1, 1, 1024), dtype=torch.int64)), **{}):
Attempting to broadcast a dimension of length 1024 at -1! Mismatching argument at index 1 had torch.Size([16, 1, 1, 1024]); but expected shape should be broadcastable to [1, 8, 16, 16]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''