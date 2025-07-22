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
        self.conv = torch.nn.Conv2d(3, 32, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(32)
        self.relu = torch.nn.ReLU(inplace=False)
        self.conv2 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.bn2 = torch.nn.BatchNorm2d(32)
        self.relu2 = torch.nn.ReLU(inplace=False)
        self.conv3 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.bn3 = torch.nn.BatchNorm2d(32)
        self.relu3 = torch.nn.ReLU(inplace=False)
        self.conv4 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.bn4 = torch.nn.BatchNorm2d(32)
        self.relu4 = torch.nn.ReLU(inplace=False)
        self.conv5 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.bn5 = torch.nn.BatchNorm2d(32)
        self.relu5 = torch.nn.ReLU(inplace=False)
        self.avgpool2d_0 = torch.nn.AvgPool2d(10, stride=14, count_include_pad=False)
        self.conv6 = torch.nn.Conv2d(32, 10, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        v3 = self.relu(v2)
        v4 = self.conv2(v3)
        v5 = self.bn2(v4)
        v6 = self.relu2(v5)
        v7 = self.conv3(v6)
        v8 = self.bn3(v7)
        v9 = self.relu3(v8)
        v10 = self.conv4(v9)
        v11 = self.bn4(v10)
        v12 = self.relu4(v11)
        v13 = self.conv5(v12)
        v14 = self.bn5(v13)
        v15 = self.relu5(v14)
        v16 = self.avgpool2d_0(v15)
        v17 = self.conv6(v16)
        v18 = v17.mean(2).expand((- 1), (- 1), 64)
        v19 = (3 + v18)
        v20 = torch.clamp_min(v19, 0)
        v21 = torch.clamp_max(v20, 6)
        v22 = (v17 * v21)
        v23 = (v22 / 6)
        return v23




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The expanded size of the tensor (64) must match the existing size (5) at non-singleton dimension 2.  Target sizes: [-1, -1, 64].  Tensor sizes: [1, 10, 5]

jit:
Failed running call_method expand(*(FakeTensor(..., device='cuda:0', size=(1, 10, 5)), -1, -1, 64), **{}):
expand: attempting to expand a dimension of length 5!

from user code:
   File "<string>", line 55, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''