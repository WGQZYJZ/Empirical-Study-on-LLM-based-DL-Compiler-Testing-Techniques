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
        self.conv1 = torch.nn.Conv2d(3, 32, 3, 1, 1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = torch.mm(v2, torch.randn(32, 28))
        v4 = v3 - 1
        v5 = F.relu(v4)
        v6 = v5 - 13
        v7 = F.relu(v6)
        v8 = F.tanh(v7)
        v9 = v8 + 1
        v10 = torch.mm(v9, torch.randn(10, 32))
        v11 = v10 - 0
        v12 = F.relu(v11)
        v13 = torch.sigmoid(v12)
        return v13



func = Model().to('cpu')


x1 = torch.randn(100, 3, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7003caf96ec0>(*(FakeTensor(..., size=(100, 32, 28, 28)), FakeTensor(..., size=(32, 28))), **{}):
a must be 2D

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''