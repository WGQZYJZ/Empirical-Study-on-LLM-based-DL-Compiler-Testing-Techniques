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
        self.linear = torch.nn.Linear(5, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - other)
        return v1



func = Model().to('cuda')




__input__ = torch.nn.Parameter(torch.randn(1, 5))



x1 = torch.randn(1, 5)


test_inputs = [__input__, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''