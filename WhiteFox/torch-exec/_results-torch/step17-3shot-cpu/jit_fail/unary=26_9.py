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

    def __init__(self, conv_transpose):
        super().__init__()
        self.conv_transpose = conv_transpose

    def forward(self, x1):
        x2 = self.conv_transpose(x1)
        x3 = x2 > 0
        x4 = x2 * 0.25
        x5 = torch.where(x3, x2, x4)
        return x5


conv_transpose = 1

func = Model(conv_transpose).to('cpu')


x1 = torch.randn(16, 3, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'int' object is not callable

jit:
'int' object is not callable
'''