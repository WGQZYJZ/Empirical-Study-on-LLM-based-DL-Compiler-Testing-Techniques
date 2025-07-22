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
        self.layers = nn.Linear(2, 4)

    def forward(self, x):
        x = self.layers(x)
        if x.ndim == 2:
            x = x.flatten()
            x = x.unsqueeze(0)
            x = [x]
        x = torch.cat(x, dim=0)
        return x



func = Model().to('cpu')


x = torch.randn(1, 2)

x1 = torch.randn(2, 2)

x2 = torch.randn(3, 2)

test_inputs = [x, x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''