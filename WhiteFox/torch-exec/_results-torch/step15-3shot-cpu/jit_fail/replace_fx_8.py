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

    def forward(self):
        p1 = torch.rand_like(x1)
        p2 = torch.rand_like(x1)
        p3 = torch.rand_like(x1)
        p4 = torch.rand_like(x1)
        p5 = torch.rand_like(x1)
        p6 = torch.rand_like(x1)
        p7 = p3 + p4
        p8 = torch.rand_like(x1)
        p9 = torch.rand_like(x1) + p7
        p10 = p5 + p6
        return p2 * p8 + p9 * p10



func = Model().to('cpu')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''