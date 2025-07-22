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

    def forward(self, x, y=None):
        c1 = torch.nn.functional.dropout(x, p=0.2)
        c2 = torch.nn.functional.dropout(x, p=0)
        a = torch.pow(6, c1) * c2
        return a



func = model().to('cuda')


x1 = torch.randn(1, 5, 10, 10)

x1_t = torch.randn(1, 5)

x = torch.randn(1)

test_inputs = [x1, x1_t, x]

# JIT_FAIL
'''
direct:
forward() takes from 2 to 3 positional arguments but 4 were given

jit:
forward() takes from 2 to 3 positional arguments but 4 were given
'''