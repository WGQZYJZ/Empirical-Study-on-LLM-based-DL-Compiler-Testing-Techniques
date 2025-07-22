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

    def __init__(self, dim, dropout):
        super().__init__()
        self.dim = dim
        self.dropout = torch.nn.Dropout2d(dropout)

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        inv_scale_factor = torch.sqrt(torch.FloatTensor(self.dim))
        scaled_qk = qk / inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(x2)
        return output


dim = 1
dropout = 1

func = Model(dim, dropout).to('cpu')


x1 = torch.randn(56, 34, 24)

x2 = torch.randn(29, 34, 25)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (56) must match the size of tensor b (29) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x78450b996ec0>(*(FakeTensor(..., size=(56, 34, 24)), FakeTensor(..., size=(29, 25, 34))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''