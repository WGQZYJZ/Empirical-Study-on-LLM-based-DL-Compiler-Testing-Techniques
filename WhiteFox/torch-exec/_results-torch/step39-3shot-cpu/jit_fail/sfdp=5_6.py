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
        self.heads = 512
        self.seq_len = 512
        self.dim = 512 // self.heads

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.740220094328575, True)
        output = attn_weight @ value
        return output



func = Model().to('cpu')


query = torch.randn(1, 64, 256, 128)

key = torch.randn(1, 256, 256, 128)

value = torch.randn(1, 64, 256, 128)

attn_mask = torch.randn(1, 1, 256, 256)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (256) at non-singleton dimension 1

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, s3, s4, s5)), FakeTensor(..., size=(1, s0, s2, s1))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''