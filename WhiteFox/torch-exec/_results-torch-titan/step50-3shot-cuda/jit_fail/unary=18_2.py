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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.maxpool = nn.MaxPool2d(2)
        self.linear1 = nn.Linear(((32 * 4) * 4), 16)
        self.linear2 = nn.Linear(16, 128)
        self.linear3 = nn.Linear(128, 2)

    def forward(self, x):
        x = F.relu_(self.conv1(x))
        x = F.relu_(self.conv2(x))
        x = self.maxpool(x)
        x = torch.flatten(x, 1)
        x = F.relu_(self.linear1(x))
        x = F.relu_(self.linear2(x))
        x = self.linear3(x)
        x = F.softmax(x, dim=0)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x32768 and 512x16)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 32768)),), **{}):
a and b must have same reduction dim, but got [1, 32768] X [512, 16].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''