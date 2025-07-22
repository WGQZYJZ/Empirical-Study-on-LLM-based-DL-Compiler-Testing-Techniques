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
        self.conv0 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv0(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1(v2)
        v4 = torch.relu(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 3, 256, 240)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv1'

jit:
'Model' object has no attribute 'conv1'
'''