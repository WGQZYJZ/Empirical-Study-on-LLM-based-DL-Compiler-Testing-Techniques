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

    def __init__(self, scale_factor, dropout_p):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, x, y):
        v1 = torch.matmul(x, y.transpose(-2, -1))
        v2 = v1 * self.scale_factor
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=self.dropout_p)
        v5 = torch.matmul(v4, y)
        return v5


scale_factor = 1
dropout_p = 1

func = Model(scale_factor, dropout_p).to('cpu')


x = torch.randn(1, 32, 3, 48, 3)

y = torch.randn(1, 64, 3, 24, 12)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x76b4acf96ec0>(*(FakeTensor(..., size=(1, 32, 3, 48, 3)), FakeTensor(..., size=(1, 64, 3, 12, 24))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''