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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 32, (3, 3), stride=(3, 3))

    def forward(self, x):
        x1 = self._tanh(self.conv(x))
        return x1



func = ModelTanh().to('cpu')


x = torch.randn(1, 3, 64, 64, requires_grad=True)

test_inputs = [x]

# JIT_FAIL
'''
direct:
'ModelTanh' object has no attribute '_tanh'

jit:
'ModelTanh' object has no attribute '_tanh'
'''