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

    def forward(self, query, key, value, attention_mask):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 / math.sqrt(query.size(-1))
        v3 = v2 + attention_mask
        v4 = torch.softmax(v3, dim=-1)
        v5 = torch.matmul(v4, value)
        return v5


func = Model().to('cpu')


query = torch.randn(1, 8, 60, 64)

key = torch.randn(1, 8, 60, 64)

value = torch.randn(1, 8, 60, 64)

attention_mask = torch.Tensor([[0, 0, 0, -10000, -10000], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

test_inputs = [query, key, value, attention_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (60) must match the size of tensor b (5) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 60, 60)), FakeTensor(..., size=(8, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([8, 5]); but expected shape should be broadcastable to [1, 8, 60, 60]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''