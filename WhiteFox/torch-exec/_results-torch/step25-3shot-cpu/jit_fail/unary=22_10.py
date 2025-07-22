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
        self.linear = torch.nn.Linear(23, 3)

    def forward(self, x1):
        (v1, v2) = self.linear
        v3 = v1 * 0.5
        v4 = v3 * v2
        v5 = torch.tanh(x1)
        v6 = v4 * v5
        return v6


func = Model().to('cpu')


x1 = torch.randn(1, 23)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
cannot unpack non-iterable Linear object

jit:
cannot unpack non-iterable Linear object
'''