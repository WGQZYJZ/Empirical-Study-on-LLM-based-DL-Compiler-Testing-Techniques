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
        self.conv = torch.nn.Conv2d(16, 16, 1, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.transpose(v1, 1, 2)
        v3 = torch.relu(v1)
        v4 = torch.matmul(v3, v2)
        v5 = v4 + v3
        v6 = torch.relu(v5)
        return v6



func = Model().to('cpu')


x = torch.randn(1, 16, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x77e58df96ec0>(*(FakeTensor(..., size=(1, 16, 64, 64)), FakeTensor(..., size=(1, 64, 16, 64))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''