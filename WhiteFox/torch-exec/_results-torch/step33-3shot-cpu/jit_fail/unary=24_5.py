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
        self.conv = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)

    def forward(self, x):
        from random import random
        negative_slope = random.random() * 1
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 32, 50, 50)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'builtin_function_or_method' object has no attribute 'random'

jit:
'builtin_function_or_method' object has no attribute 'random'
'''