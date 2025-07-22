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
        self.conv1 = torch.nn.Conv2d(32, 256, 4, stride=3, padding=3)
        self.conv2 = torch.nn.Conv2d(256, 128, 3, stride=3, padding=1)
        self.fc = torch.nn.Linear(27, 100)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2
        v5 = v4 * v2
        v6 = v5 * 0.044715
        v7 = v2 + v6
        v8 = v7 * 0.7978845608028654
        v9 = torch.tanh(v8)
        v10 = v9 + 1
        v11 = v3 * v10
        v12 = v11.view(-1, 27)
        v13 = self.fc(v12)
        return v13



func = Model().to('cpu')


x1 = torch.randn(10, 32, 11, 11)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 27]' is invalid for input of size 5120

jit:
Failed running call_method view(*(FakeTensor(..., size=(s0, 128, (((s2 + 2)//9)) + 1, (((s3 + 2)//9)) + 1)), -1, 27), **{}):
shape '[-1, 27]' is invalid for input of size 128*s0*((((s2 + 2)//9)) + 1)*((((s3 + 2)//9)) + 1)

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''