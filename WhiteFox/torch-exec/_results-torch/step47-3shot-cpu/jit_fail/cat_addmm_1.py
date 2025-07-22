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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 2)
        self.activation = nn.Tanh()

    def forward(self, x):
        x = self.layers(x)
        x = self.activation(x)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2, requires_grad=True)

y = torch.randn(2, 4, requires_grad=True)

z = torch.randn(2, 5, requires_grad=True)

test_inputs = [x, y, z]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''