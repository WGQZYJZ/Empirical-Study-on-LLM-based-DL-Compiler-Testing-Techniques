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
        self.conv1 = torch.nn.Conv2d(3, 3, 4)
        self.conv2 = torch.nn.Conv2d(3, 3, 3)
        self.conv3 = torch.nn.Conv2d(3, 3, 2, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 3, 1)
        self.bn1 = torch.nn.BatchNorm2d(3)
        self.bn2 = torch.nn.BatchNorm3d(3)
        self.bn3 = torch.nn.BatchNorm3d(3)

    def forward(self, x1):
        s1 = self.conv1(x1)
        s2 = self.conv2(s1)
        s3 = self.conv3(s2)
        s = self.bn1(s3)
        t = self.conv4(s)
        t = torch.sub(t, 0.001)
        t = torch.div(t, 0.001)
        y = self.bn2(t)
        return s



func = Model().to('cpu')


x1 = torch.randn(1, 3, 8, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected 5D input (got 4D input)

jit:
expected 5D input (got 4D input)
'''