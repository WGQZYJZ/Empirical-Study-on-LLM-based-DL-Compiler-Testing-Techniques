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
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x1, x3):
        v1 = self.conv1(x1)
        v3 = (v1 + x3)
        v4 = torch.relu(v3)
        v5 = self.conv1(v4)
        v6 = (v5 + x3)
        v8 = torch.relu(v6)
        v9 = self.conv2(v8)
        v10 = (v9 + x2)
        v11 = torch.relu(v10)
        return v11




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = torch.tanh(v1)
        v4 = torch.tanh(v1)
        v5 = torch.softmax(v4, dim=0)
        v6 = (v5 + v3)
        v7 = torch.tanh(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x3]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''