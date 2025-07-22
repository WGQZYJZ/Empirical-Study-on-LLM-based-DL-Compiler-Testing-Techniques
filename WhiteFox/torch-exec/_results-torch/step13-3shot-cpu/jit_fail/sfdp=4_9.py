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

    def __init__(self, batch_size=2, num_heads=2, query_len=8, key_len=8, channel=2):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(batch_size, num_heads, query_len, channel))
        self.key = torch.nn.Parameter(torch.randn(batch_size, num_heads, key_len, channel))
        self.value = torch.nn.Parameter(torch.randn(batch_size, num_heads, query_len, channel))

    def forward(self, qk, attn_mask):
        qk = qk @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ self.value
        return output


func = Model().to('cpu')


qk = torch.randn(2, 2, 8, 2)

attn_mask = torch.randn(2, 2, 8)

test_inputs = [qk, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(2, 2, 8, 8)), FakeTensor(..., size=(2, 2, 8))), **{}):
Attempting to broadcast a dimension of length 2 at -2! Mismatching argument at index 1 had torch.Size([2, 2, 8]); but expected shape should be broadcastable to [2, 2, 8, 8]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''