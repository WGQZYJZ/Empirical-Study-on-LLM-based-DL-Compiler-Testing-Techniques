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

    def forward(self, inputs):
        (x, y, z) = inputs
        x1 = x * y
        x2 = x + z
        y1 = x * z
        z1 = y * z
        o1 = (x1 + x2) * z
        o2 = (y1 + z1) * x
        o3 = o1 + o2
        return o3



func = Model().to('cpu')

inputs = 1

test_inputs = [inputs]

# JIT_FAIL
'''
direct:
cannot unpack non-iterable int object

jit:
cannot unpack non-iterable int object
'''