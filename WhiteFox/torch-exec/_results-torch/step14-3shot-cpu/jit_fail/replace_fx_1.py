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

class model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self):
        x1 = torch.rand(1, 2, 2)
        x2 = torch.rand(1, 2, 2)
        x3 = torch.rand_like(x1)
        x4 = torch.rand(1, 2, 2)
        x5 = torch.zeros(1, 2, 2)
        x6 = torch.rand_like(x1)
        return x6



func = model().to('cpu')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''