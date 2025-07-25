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
        torch.manual_seed(0)
        self.conv1_1 = torch.nn.Conv2d(3, 16, kernel_size=3, stride=1)
        self.bn1_1 = torch.nn.BatchNorm2d(16)
        torch.manual_seed(0)
        self.conv2_1 = torch.nn.Conv2d(64, 16, kernel_size=3, stride=1)
        self.bn1_2 = torch.nn.BatchNorm2d(16)
        torch.manual_seed(0)
        self.conv3_1 = torch.nn.Conv2d(128, 3, kernel_size=3, stride=1)
        self.bn2_1 = torch.nn.BatchNorm2d(3)
        self.relu1 = torch.nn.ReLU(inplace=False)

    def forward(self, x):
        v1 = self.conv1_1(x)
        v2 = self.bn1_1(v1)
        v3 = v1 + v2
        v4 = self.relu1(v3)
        v5 = torch.nn.functional.interpolate(v4, size=[x.size()[2]], mode='bicubic')
        v6 = self.conv2_1(v5)
        v6 = self.bn1_2(v6)
        v6 = self.conv3_1(v6)
        v7 = v5 + v6
        v8 = self.bn2_1(v7)
        v8 = self.conv1_1(v8)
        v9 = torch.nn.functional.interpolate(v8, size=[x.size()[2]], mode='bicubic')
        v10 = self.conv2_1(v9)
        v11 = self.conv1_1(v10)
        v12 = self.conv1_1(v11)
        v13 = torch.nn.functional.interpolate(v12, scale_factor=2, mode='bilinear')
        v14 = self.conv1_1(v13)
        v15 = self.conv1_1(v14)
        v16 = torch.nn.functional.interpolate(v15, scale_factor=2, mode='nearest')
        v17 = self.conv1_1(v16)
        return v17



func = Model().to('cpu')


x1 = torch.randn(1, 3, 17, 17)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input and output must have the same number of spatial dimensions, but got input with spatial dimensions of [15, 15] and output size of [17]. Please provide input tensor in (N, C, d1, d2, ...,dK) format and output size in (o1, o2, ...,oK) format.

jit:
Failed running call_function <function interpolate at 0x7e36756840d0>(*(FakeTensor(..., size=(1, 16, 15, 15)),), **{'size': [17], 'mode': 'bicubic'}):
Input and output must have the same number of spatial dimensions, but got input with spatial dimensions of [15, 15] and output size of [17]. Please provide input tensor in (N, C, d1, d2, ...,dK) format and output size in (o1, o2, ...,oK) format.

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''