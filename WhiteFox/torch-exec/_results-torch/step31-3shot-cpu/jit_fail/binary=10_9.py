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

    def __init__(self, other_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other_tensor = other_tensor

    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = t1 + self.other_tensor
        return t2


other_tensor = torch.randn(8, 3)
func = Model(other_tensor).to('cpu')


other_tensor = torch.randn(8, 3)

x1 = torch.randn(1, 3, 64, 64)

test_inputs = [other_tensor, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''