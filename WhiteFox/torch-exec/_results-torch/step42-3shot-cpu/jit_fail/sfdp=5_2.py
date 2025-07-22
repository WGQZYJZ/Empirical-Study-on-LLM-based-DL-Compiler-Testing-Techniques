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
        self.heads = 256
        self.seq_len = 128
        self.dim = 1024 // self.heads

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.2, True)
        output = attn_weight @ value
        return output



func = Model().to('cpu')


query = torch.randn(1, 256, 32, 32, 1024)

key = torch.randn(1, 256, 32, 32, 1024)

value = torch.randn(1, 256, 32, 32, 1024)

attn_mask = torch.randn(1, 1, 256, 32, 32)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (256) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 256, 32, 32, 32)), FakeTensor(..., size=(1, 1, 256, 32, 32))), **{}):
Attempting to broadcast a dimension of length 256 at -3! Mismatching argument at index 1 had torch.Size([1, 1, 256, 32, 32]); but expected shape should be broadcastable to [1, 256, 32, 32, 32]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''