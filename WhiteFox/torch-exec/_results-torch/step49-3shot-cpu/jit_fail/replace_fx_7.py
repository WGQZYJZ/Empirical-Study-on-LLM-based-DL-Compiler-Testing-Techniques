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

    def forward(self, x, y):
        a = torch.rand_like(x)
        b = torch.rand_like(y)
        return 1



func = Model().to('cpu')


y1 = torch.randn(1, 2, 2)
x = 1

test_inputs = [y1, x]

# JIT_FAIL
'''
direct:
rand_like(): argument 'input' (position 1) must be Tensor, not int

jit:
rand_like(): argument 'input' (position 1) must be Tensor, not int
'''