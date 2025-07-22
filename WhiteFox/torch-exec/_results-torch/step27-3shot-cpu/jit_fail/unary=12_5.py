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
        self.conv1 = torch.nn.Conv2d(3, 64, 48, 4, 26, groups=1)
        self.conv2 = torch.nn.ConvTranspose2d(64, 32, 48, 4, 26, groups=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.relu(v1)
        v3 = self.conv2(v2)
        v4 = F.sigmoid(v3)
        v5 = v1 * v4
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 120, 120)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (120) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 64, ((s0//4)) + 2, ((s1//4)) + 2)), FakeTensor(..., size=(1, 32, 4*((s0//4)), 4*((s1//4))))), **{}):
The size of tensor a (((s1//4)) + 2) must match the size of tensor b (4*((s1//4))) at non-singleton dimension 3)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''