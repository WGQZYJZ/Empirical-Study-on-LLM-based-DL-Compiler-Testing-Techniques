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

    def forward(self, t1, t2):
        a = torch.mm(t1, t2)
        b = torch.mm(t2, t1)
        return torch.mm(a, b)



func = Model().to('cpu')


x = torch.randn(1, 1)

y = torch.randn(1, 1)

z = torch.randn(1, 1)

test_inputs = [x, y, z]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''