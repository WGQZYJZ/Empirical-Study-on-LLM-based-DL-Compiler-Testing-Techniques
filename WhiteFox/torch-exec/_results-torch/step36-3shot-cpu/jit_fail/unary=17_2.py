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
        self.conv = nn.ConvTranspose1d(3, 25, 5, stride=2, padding=2)

    def forward(self, x1):
        v1 = F.relu(self.conv1(x1))
        v2 = F.relu(self.conv2(v1))
        v3 = F.relu(self.conv3(v2))
        v4 = F.relu(self.conv4(v3))
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 3, 51)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv1'

jit:
'Model' object has no attribute 'conv1'
'''