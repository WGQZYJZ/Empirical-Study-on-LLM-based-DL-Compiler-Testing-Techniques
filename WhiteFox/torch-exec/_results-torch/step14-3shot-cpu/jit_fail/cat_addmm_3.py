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

class SubModel(nn.Module):

    def forward(self, x):
        t1 = torch.addmm(x, t, u)
        t2 = torch.cat((t1, t1, t1), dim=1)
        return t2

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.submodel = SubModel()

    def forward(self, x):
        return self.submodel(x)



func = Model().to('cpu')


x = torch.randn(2, 2)

t = torch.rand(4, 2)

u = torch.rand(4, 2)

test_inputs = [x, t, u]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''