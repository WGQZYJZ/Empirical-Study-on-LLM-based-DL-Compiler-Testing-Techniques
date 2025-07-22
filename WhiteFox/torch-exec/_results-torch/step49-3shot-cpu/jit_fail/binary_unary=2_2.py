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
        self.conv1 = torch.nn.Conv2d(3, 64, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 64, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(64, 64, 3, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(64, 32, 4, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(32, 16, 4, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(16, 3, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - 10
        v3 = F.relu(v2)
        v4 = self.conv2(v3)
        v5 = v4 - 20
        v6 = F.relu(v5)
        v7 = self.conv3(v6)
        v8 = v7 - 7
        v9 = F.relu(v8)
        v10 = self.conv4(v9)
        v11 = v10 - 30
        v12 = F.relu(v11)
        v13 = self.conv5(v12)
        v14 = v13 - 19
        v15 = F.relu(v14)
        v16 = torch.cat((v15, v6), 1)
        v17 = torch.squeeze(v16, 0)
        v18 = self.conv6(v17)
        v19 = torch.mean(v18, (2, 3))
        return v19



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 54 but got size 112 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x716208996ec0>(*((FakeTensor(..., size=(1, 16, 54, 54)), FakeTensor(..., size=(1, 64, 112, 112))), 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 54 in dimension 2 but got 112 for tensor number 1 in the list

from user code:
   File "<string>", line 40, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''