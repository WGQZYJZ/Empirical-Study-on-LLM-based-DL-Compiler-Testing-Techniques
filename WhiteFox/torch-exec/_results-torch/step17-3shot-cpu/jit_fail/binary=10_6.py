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
        self.linear1 = torch.nn.Linear(64, 32)

    def forward(self, x2):
        v1 = self.linear1(x2)
        v2 = v1 + 0.1
        return v2


func = Model().to('cpu')


x2 = torch.randn(1, 64)

other = torch.randn(1, 32)

test_inputs = [x2, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''