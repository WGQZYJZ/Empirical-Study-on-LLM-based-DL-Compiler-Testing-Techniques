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
        self.seq_len = 512
        self.dim = 128 // self.heads

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = attn_weight @ value
        return output



func = Model().to('cpu')


query = torch.randn(8, 64, 1024, 128)

key = torch.randn(8, 64, 1024, 8)

value = torch.randn(8, 64, 1024, 128)

attn_mask = torch.randn(8, 1, 1024, 1024)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [512, 128] but got: [512, 8].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(s0, s1, s6, s7)), FakeTensor(..., size=(s0, s1, s3, s2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0*s1, s7] but got: [s0*s1, s3].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''