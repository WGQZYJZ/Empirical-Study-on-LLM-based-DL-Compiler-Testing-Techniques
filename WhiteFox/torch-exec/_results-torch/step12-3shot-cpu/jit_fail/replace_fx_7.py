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

    def __init__(self, d=0.5):
        super().__init__()
        self.d = d

    def forward(self, input_tensor):
        x = torch.rand_like(input_tensor)
        return x > self.d



func = Model().to('cpu')


x1 = torch.randn((3, 4))

x2 = torch.randn((5, 3, 4))

x3 = torch.randn((7, 7, 4))

x4 = torch.randn((8, 3, 2, 4))

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''