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

    def forward(self, x1, x2, x3):
        v1 = torch.mm(y1, x2)
        v2 = torch.mm(y2, x3)
        v3 = v1 + v2
        return v3



func = Model().to('cpu')


y1 = torch.randn(3, 3)

y2 = torch.randn(3, 3)

x1 = torch.randn(3, 3, requires_grad=True)

x2 = torch.randn(3, 3)

x3 = torch.randn(3, 3)

test_inputs = [y1, y2, x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 4 positional arguments but 6 were given

jit:
forward() takes 4 positional arguments but 6 were given
'''