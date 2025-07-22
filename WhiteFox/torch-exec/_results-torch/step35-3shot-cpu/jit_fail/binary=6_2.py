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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, _input):
        v1 = self.linear(_input)
        v2 = v1 - other
        return v2


func = Model().to('cpu')


__input01__ = torch.randn(1, 3)

__input02__ = torch.randn(3)

test_inputs = [__input01__, __input02__]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''