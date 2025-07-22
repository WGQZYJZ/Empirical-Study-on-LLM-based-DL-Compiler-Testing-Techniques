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

    def __init__(self, query_channels, key_channels):
        super().__init__()
        self.query_channels = query_channels
        self.key_channels = key_channels

    def forward(self, query, key, value, dropout_p=0.0):
        q = query.unsqueeze(2)
        k = key.unsqueeze(1)
        w = torch.matmul(q, k).div(self.query_channels ** 0.25)
        w = torch.nn.functional.dropout(w, p=dropout_p)
        w = w.softmax(dim=-1)
        v = torch.matmul(w, value.unsqueeze(-1)).squeeze(-1)
        return v


query_channels = 1
key_channels = 1
func = Model(3, 4).to('cpu')


query = torch.randn(1, 4, 8)

key = torch.randn(1, 8, 4)

value = torch.randn(1, 8, 5)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7c896ab96ec0>(*(FakeTensor(..., size=(1, 4, 1, 4)), FakeTensor(..., size=(1, 8, 5, 1))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''