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

    def __init__(self, t0):
        super().__init__()
        self.t0 = t0

    def forward(self, x):
        t0 = torch.cat([x, x, x, x], dim=0)
        t1 = t0.view(-1, t0.shape[0])
        t2 = t0.view(-1)
        t0 = torch.cat((x, x), dim=1)
        t3 = torch.relu(t2)
        return t3


t0 = torch.randn(2, 3, 4)

func = Model(t0).to('cpu')


t0 = torch.randn(2, 3, 4)

x = torch.randn(2, 3, 4)

test_inputs = [t0, x]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''