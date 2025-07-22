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

    def forward(self, x):
        with torch.no_grad():
            x1 = torch.nn.functional.conv_transpose2d(x, self.conv_t.weight, None, bias=None, stride=1, dilation=1, groups=1)
        x2 = x1 > 0
        x3 = x1 * 5.398
        x4 = torch.where(x2, x1, x3)
        return x4



func = Model().to('cpu')


x = torch.randn(4, 3, 10, 20)

test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv_t'

jit:
'Model' object has no attribute 'conv_t'
'''