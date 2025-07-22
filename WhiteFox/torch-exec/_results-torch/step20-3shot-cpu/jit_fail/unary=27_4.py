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

    def __init__(self, min_clamp=0.7, max_clamp=0.6):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(5, 4, 1, stride=1, padding=0, bias=True)
        self.conv2 = torch.nn.Conv2d(4, 8, 3, stride=1, padding=1, bias=True)
        self.conv3 = torch.nn.Conv2d(4, 8, 3, stride=1, padding=2, bias=True)
        self.min_clamp = torch.zeros(8) + min_clamp
        self.max_clamp = torch.zeros(8) + max_clamp

    def forward(self, x1):
        v1 = torch.nn.functional.relu(self.conv1(x1))
        v2 = torch.nn.functional.relu(self.conv2(v1))
        v3 = torch.nn.functional.relu(self.conv3(v1))
        v4 = self.min_clamp.reshape(1, 8, 1, 1)
        return F.relu(torch.clamp(v2 * v3 + v4, min=self.min_clamp, max=self.max_clamp))



func = Model().to('cpu')


x1 = torch.randn(2, 5, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (8) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(s0, 8, s2, s3)), FakeTensor(..., size=(s0, 8, s2 + 2, s3 + 2))), **{}):
The size of tensor a (s3) must match the size of tensor b (s3 + 2) at non-singleton dimension 3)

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''