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
        self.conv3 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = v5 + x
        v7 = torch.relu(v6)
        return v7

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.sigmoid(v1)
        v3 = 1 - v2
        v4 = self.conv2(v3)
        v5 = torch.sigmoid(v4)
        v6 = 1 - v5
        v7 = self.conv3(v6)
        v8 = torch.sigmoid(v7)
        v9 = 1 - v8
        v10 = 1 + v8
        v11 = v9 + v10
        return v11

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv4 = nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv5 = nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, i1, i2):
        o1 = self.conv1(i1)
        o2 = self.conv2(o1)
        o3 = self.conv3(o2)
        o4 = self.conv4(o3)
        o5 = self.conv5(o4)
        o6 = o5 + i2
        o7 = nn.ReLU()(o6)
        return o7

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v6 = self.conv5(v4)
        v7 = v6 + x
        v8 = torch.relu(v7)
        return v8



func = Model().to('cpu')


x = torch.randn(1, 16, 64, 64)

i1 = torch.randn(1, 16, 64, 64)

i2 = torch.randn(1, 16, 64, 64)

test_inputs = [x, i1, i2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''