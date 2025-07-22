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
        self.linear = torch.nn.Linear(3, 5)
        self.bn = torch.nn.BatchNorm2d(5)

    def forward(self, x1):
        x2 = self.linear(x1)
        x3 = self.bn(x2)
        x4 = torch.relu(x3)
        return x4


func = Model().to('cpu')


x1 = torch.randn(20, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected 4D input (got 2D input)

jit:
expected 4D input (got 2D input)
'''