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
        self.linear = torch.nn.Linear(10, 5)
        self.other = other

    def forward(self, x):
        v1 = self.linear(x)
        return torch.nn.functional.relu((v1 + self.other))




other = torch.nn.Parameter(torch.zeros(5))

func = Model(other).to('cuda')




other = torch.nn.Parameter(torch.zeros(5))



x = torch.randn(1, 10)


test_inputs = [other, x]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''