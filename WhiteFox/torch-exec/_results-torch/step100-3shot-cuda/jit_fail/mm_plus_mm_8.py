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

    def __init__(self, weight):
        super(Model, self).__init__()
        self.weight = weight

    def forward(self, x):
        out = torch.mm(x, self.weight)
        return out


weight = torch.randn(1000, 1000)

func = Model(weight).to('cuda')


weight = torch.randn(1000, 1000)

x = torch.randn(100, 100)

test_inputs = [weight, x]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''