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

    def forward(self, x1):
        lstm1 = torch.nn.LSTMCell(2, 5)
        v1 = lstm1(x1)
        v2 = torch.reshape(v1, (5,))
        v3 = v2.mean()
        v2 = v2.add(v3)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 2, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
LSTMCell: Expected input to be 1D or 2D, got 3D instead

jit:
LSTMCell: Expected input to be 1D or 2D, got 3D instead
'''