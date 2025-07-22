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
        self.bn = torch.nn.BatchNorm2d(3)
        self.conv = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1)
        self.avgpool = torch.nn.AvgPool2d(5, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(64, 8, 2, stride=1, padding=0)
        self.dropout = torch.nn.Dropout2d(0.25, False)
        self.conv3 = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
        self.fc = torch.nn.Linear(64, 3)

    def forward(self, x1):
        v1 = self.bn(x1)
        v2 = torch.nn.functional.interpolate(v1, size=None, scale_factor=2.0, recompute_scale_factor=None, mode='bilinear', align_corners=None)
        v3 = self.conv(v2)
        v4 = self.avgpool(v3)
        v5 = self.conv2(v4)
        v6 = torch.relu(v5)
        v7 = self.dropout(v6)
        v8 = self.conv3(v7)
        v9 = torch.relu(v8)
        v10 = torch.flatten(v9, 1)
        v11 = self.fc(v10)
        return v11



func = Model().to('cpu')


x1 = torch.randn(1, 3, 144, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2346512 and 64x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2346512)), Parameter(FakeTensor(..., size=(3, 64), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 2346512] X [64, 3].

from user code:
   File "<string>", line 36, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''