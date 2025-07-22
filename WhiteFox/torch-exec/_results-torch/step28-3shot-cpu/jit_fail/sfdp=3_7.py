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

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 * 1.0
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.7)
        v5 = v4.matmul(v1)
        return v5


func = Model().to('cpu')


x1 = torch.randn(32, 3, 256)

x2 = torch.randn(256, 8, 512)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (256) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x7d5898196ec0>(*(FakeTensor(..., size=(32, 3, 256)), FakeTensor(..., size=(256, 512, 8))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''