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
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        return torch.matmul(dropout_qk, value)


func = Model().to('cpu')


query = torch.randn(1, 3, 64, 64)

key = torch.randn(1, 3, 64, 64)

value = torch.randn(1, 3, 64, 64)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (7) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 3, 64, 64)), FakeTensor(..., size=(1, 1, 5, 7))), **{}):
Attempting to broadcast a dimension of length 7 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 5, 7]); but expected shape should be broadcastable to [1, 3, 64, 64]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''