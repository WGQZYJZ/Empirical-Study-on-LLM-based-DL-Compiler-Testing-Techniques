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

    def forward(self, x):
        w1 = torch.rand_like(x, dtype=torch.float)
        y = torch.nn.functional.dropout(x, p=0.8, training=True)
        z = w1 + y
        return z



func = Model().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
rand_like(): argument 'input' (position 1) must be Tensor, not int

jit:
rand_like(): argument 'input' (position 1) must be Tensor, not int
'''