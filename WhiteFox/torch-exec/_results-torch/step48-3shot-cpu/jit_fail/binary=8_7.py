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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.bn3 = torch.nn.BatchNorm2d(8)
        self.bn4 = torch.nn.BatchNorm2d(8)
        self.relu1 = torch.nn.ReLU()
        self.relu2 = torch.nn.ReLU()
        self.conv7 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 + x1
        v3 = self.bn1(v2)
        v4 = self.relu2(v3)
        v5 = self.bn2(v4)
        v6 = torch.tanh(v5)
        v7 = self.relu1(v6)
        v8 = self.conv2(v7)
        v9 = self.conv3(x1)
        v10 = v8 - v9
        v11 = self.bn3(v10)
        v12 = self.bn4(v10)
        v13 = v11 % v12
        v14 = self.conv4(v7)
        v15 = torch.sigmoid(v14)
        v16 = self.conv5(v15)
        v17 = v13 * v16
        v18 = self.conv6(v16)
        v19 = torch.relu(v18)
        v20 = self.conv7(v19)
        return v20



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (66) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 66, 66)), FakeTensor(..., size=(1, 3, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 64, 64]); but expected shape should be broadcastable to [1, 8, 66, 66]

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''