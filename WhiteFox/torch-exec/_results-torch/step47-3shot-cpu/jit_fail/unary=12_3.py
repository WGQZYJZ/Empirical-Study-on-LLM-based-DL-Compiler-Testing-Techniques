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
        self.conv = torch.nn.Conv2d(4, 3, (3, 3), stride=(2, 2), padding=(1, 1))
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.relu(v1)
        v3 = v1 * v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 4, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'relu'

jit:
'Model' object has no attribute 'relu'
'''