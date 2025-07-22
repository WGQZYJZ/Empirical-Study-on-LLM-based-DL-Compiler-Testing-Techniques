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

class ModelM(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1_A1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv1_B1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv1_C1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1a1 = self.conv1_A1(x1)
        v1b1 = self.conv1_B1(x1)
        v1c1 = self.conv1_C1(x1)
        v1 = v1a1 + v1b1 + v1c1
        v2 = v1 + x2
        return v2



func = ModelM().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (66) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 66, 66)), FakeTensor(..., size=(1, 3, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 64, 64]); but expected shape should be broadcastable to [1, 8, 66, 66]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''