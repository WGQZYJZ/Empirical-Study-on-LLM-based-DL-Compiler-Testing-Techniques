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
        self.stack = torch.stack

    def forward(self, x):
        x = torch.stack((x, x), dim=0)
        x = x.view([2, -1])
        return x



func = Model().to('cpu')


x = torch.randn(2)

y = torch.randn(4)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''