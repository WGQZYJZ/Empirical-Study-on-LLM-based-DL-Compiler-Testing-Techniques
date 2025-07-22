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
        self.conv1 = torch.nn.Conv2d(3, 32, 3, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 32, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=0)
        self.conv4 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=0)
        self.conv5 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv6 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(v1)
        v4 = self.conv4(v3)
        v5 = self.conv5(v2)
        v6 = self.conv6(v5)
        v7 = v1 + v2 + v3 + v4 + v5 + v6
        v8 = torch.relu(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (111) must match the size of tensor b (112) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 32, 111, 111)), FakeTensor(..., size=(1, 32, 112, 112))), **{}):
Attempting to broadcast a dimension of length 112 at -1! Mismatching argument at index 1 had torch.Size([1, 32, 112, 112]); but expected shape should be broadcastable to [1, 32, 111, 111]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''