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
        self.lstm = torch.nn.LSTM(2, 2)

    def forward(self, x1):
        (x2, state_h) = self.lstm(x1)
        x3 = torch.rand_like(x1, requires_grad=True)
        _ = torch.cat([x2, x3], dim=1)
        return state_h._values.clone()



func = Model().to('cpu')


x1 = torch.randn(3, 3, 2, requires_grad=True)

h0 = torch.randn(2, 1, 2, requires_grad=True)

c0 = torch.randn(2, 1, 2, requires_grad=True)

test_inputs = [x1, h0, c0]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''