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
        self.conv1 = torch.nn.Conv2d(3, 128, 1, stride=1)
        self.conv2 = torch.nn.Conv2d(3, 64, 1, stride=1)
        self.conv3 = torch.nn.Conv2d(64, 8, 1, stride=1)
        self.fc1 = torch.nn.Linear(8, 128)
        self.fc2 = torch.nn.Linear(128, 10)

    def forward(self, x1):
        v1 = torch.relu(self.conv1(x1))
        v2 = torch.relu(self.conv2(x1))
        v3 = torch.relu(self.conv3(v2))
        v4 = v1.flatten(start_dim=1)
        v5 = torch.relu(self.fc1(v4))
        v6 = self.fc2(v5)
        return v6



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x524288 and 8x128)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(1, 524288)),), **{}):
a and b must have same reduction dim, but got [1, 524288] X [8, 128].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''