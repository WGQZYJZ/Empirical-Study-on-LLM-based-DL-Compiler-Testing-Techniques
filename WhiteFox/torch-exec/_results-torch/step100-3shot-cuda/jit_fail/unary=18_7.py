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

class TestModule(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4, x5, x6):
        return (torch.nn.MaxPool1d(x4, **{'kernel_size': 2, 'stride': x1}), torch.nn.MaxPool2d(**{'kernel_size': x3, 'stride': x2}), torch.nn.MaxPool3d(**{'kernel_size': (x4, x5, 5), 'stride': x6}))



func = TestModule().to('cuda')

x1 = 1
x2 = 1
x3 = 1
x4 = 1
x5 = 1
x6 = 1

test_inputs = [x1, x2, x3, x4, x5, x6]

# JIT_FAIL
'''
direct:
__init__() got multiple values for argument 'kernel_size'

jit:
__init__() got multiple values for argument 'kernel_size'
'''