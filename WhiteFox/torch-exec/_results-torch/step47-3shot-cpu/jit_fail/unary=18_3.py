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
        self.conv1 = torch.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=1, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=1, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.elu(v1)
        v3 = self.conv2(v2)
        v4 = torch.elu(v3)
        v5 = self.conv3(v4)
        v6 = torch.elu(v5)
        v7 = self.conv4(v6)
        v8 = torch.elu(v7)
        v9 = self.conv5(v8)
        v10 = torch.elu(v9)
        return v10



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'elu'

jit:
AttributeError: module 'torch' has no attribute 'elu'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''