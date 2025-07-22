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

    def __init__(self, other):
        super().__init__()
        self.other = torch.nn.Parameter(other)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, weight=self.other)
        v2 = v1 + self.other
        return v2


other = torch.randn(2)

func = Model(other).to('cpu')


x1 = torch.randn(1, 2)

other = torch.randn(2)

test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''