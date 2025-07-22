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
        self.conv1 = torch.nn.Conv2d(5, 5, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(5, 5, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(5, 5, 5, stride=1, padding=2)
        self.conv4 = torch.nn.Conv2d(5, 5, 7, stride=1, padding=3)
        self.conv5 = torch.nn.Conv2d(1, 1, 7, stride=1, padding=0)
        self.bn1 = torch.nn.BatchNorm2d(5)
        self.bn2 = torch.nn.BatchNorm2d(5)
        self.bn3 = torch.nn.BatchNorm2d(5)
        self.bn4 = torch.nn.BatchNorm2d(5)
        self.bn5 = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(x)
        v3 = self.conv3(x)
        v4 = self.conv4(x)
        v5 = self.conv5(x)
        v7 = torch.nn.functional.relu(self.bn1(v4))
        v8 = torch.nn.functional.relu(self.bn2(v5))
        v9 = torch.nn.functional.relu(self.bn3(v7))
        v10 = torch.nn.functional.relu(self.bn4(v8))
        v12 = torch.nn.functional.relu(self.bn5(v10))
        v15 = torch.nn.functional.leaky_relu(v1, 0.25)
        v16 = torch.nn.functional.leaky_relu(v2, 0.25)
        v17 = torch.nn.functional.leaky_relu(v3, 0.25)
        v18 = torch.nn.functional.leaky_relu(v15, 0.25)
        v19 = torch.nn.functional.leaky_relu(v16, 0.25)
        v20 = torch.nn.functional.leaky_relu(v17, 0.25)
        v21 = torch.nn.functional.leaky_relu(v18, 0.25)
        v22 = torch.nn.functional.leaky_relu(v19, 0.25)
        v23 = torch.nn.functional.leaky_relu(v20, 0.25)
        v24 = torch.nn.functional.leaky_relu(v21, 0.25)
        v25 = torch.nn.functional.leaky_relu(v22, 0.25)
        v26 = torch.nn.functional.leaky_relu(v23, 0.25)
        return v19




func = Model().to('cuda')



x1 = torch.randn(1, 5, 49, 49)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 7, 7], expected input[1, 5, 49, 49] to have 1 channels, but got 5 channels instead

jit:
Failed running call_module L__self___conv5(*(FakeTensor(..., device='cuda:0', size=(1, 5, 49, 49)),), **{}):
Given groups=1, weight of size [1, 1, 7, 7], expected input[1, 5, 49, 49] to have 1 channels, but got 5 channels instead

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''