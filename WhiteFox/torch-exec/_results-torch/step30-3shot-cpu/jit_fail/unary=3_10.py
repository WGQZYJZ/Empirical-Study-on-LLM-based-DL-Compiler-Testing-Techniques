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
        self.conv1 = torch.nn.Conv2d(3, 11, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(11, 9, 6, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(9, 6, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(6, 7, 1, stride=1, padding=3)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v1 = torch.nn.functional.interpolate(v1, scale_factor=2.0)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v4 = torch.nn.functional.interpolate(v4, scale_factor=0.5)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v7 = torch.nn.functional.interpolate(v7, scale_factor=0.5)
        v8 = self.conv3(v7)
        v8 = torch.nn.functional.interpolate(v8, scale_factor=0.5)
        v9 = self.conv4(v8)
        v9 = torch.nn.functional.interpolate(v9, scale_factor=0.5)
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (448) must match the size of tensor b (224) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 11, 448, 448)), FakeTensor(..., size=(1, 11, 224, 224))), **{}):
Attempting to broadcast a dimension of length 224 at -1! Mismatching argument at index 1 had torch.Size([1, 11, 224, 224]); but expected shape should be broadcastable to [1, 11, 448, 448]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''