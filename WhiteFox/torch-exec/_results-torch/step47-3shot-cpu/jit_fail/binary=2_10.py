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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x, x2=torch.randn(2, 3, 128, 128)):
        v1 = self.conv(x, padding=1, bias=None)
        v2 = v1 - x2
        return v2



func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'padding'

jit:
forward() got an unexpected keyword argument 'padding'
'''