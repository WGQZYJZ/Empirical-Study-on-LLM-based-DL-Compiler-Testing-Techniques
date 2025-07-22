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
        torch.manual_seed(1)
        self.conv = torch.nn.Conv2d(8, 8, 5)
        torch.manual_seed(1)
        self.bn = torch.nn.BatchNorm3d(8)

    def forward(self, x):
        x = self.conv(self.conv(x))
        x = self.bn(x)
        return x



func = Model().to('cpu')


x = torch.randn(1, 8, 32, 32)

test_inputs = [x]

# JIT_FAIL
'''
direct:
expected 5D input (got 4D input)

jit:
expected 5D input (got 4D input)
'''