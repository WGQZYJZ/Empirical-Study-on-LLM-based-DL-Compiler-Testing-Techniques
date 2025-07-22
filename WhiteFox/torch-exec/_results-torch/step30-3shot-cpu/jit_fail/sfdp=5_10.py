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
        self.heads = 64
        self.seq_len = 768
        self.dim = 350 // self.heads

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = attn_weight @ value
        return output



func = Model().to('cpu')


query = torch.randn(1, 64, 738, 354)

key = torch.randn(1, 64, 738, 354)

value = torch.randn(1, 64, 738, 354)

attn_mask = torch.randn(1, 1, 768, 768)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (738) must match the size of tensor b (768) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 64, 738, 738)), FakeTensor(..., size=(1, 1, 768, 768))), **{}):
Attempting to broadcast a dimension of length 768 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 768, 768]); but expected shape should be broadcastable to [1, 64, 738, 738]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''