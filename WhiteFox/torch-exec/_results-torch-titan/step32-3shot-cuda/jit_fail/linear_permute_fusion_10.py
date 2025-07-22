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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        lstm1 = torch.nn.LSTMCell(2, 2)
        v3 = lstm1(v1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
LSTMCell: Expected input to be 1D or 2D, got 3D instead

jit:
LSTMCell: Expected input to be 1D or 2D, got 3D instead
'''