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
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(100, 200, bias=True)
        self.conv = torch.nn.Conv2d(3, 3, 5, stride=5, padding=1, bias=False)

    def forward(self, x):
        x = torch.relu(self.linear(x))
        return torch.relu(self.conv(x))



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

x2 = torch.randn(1, 100)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''