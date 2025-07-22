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

class MyAwesomeModel(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x1 = torch.nn.functional.dropout(x, p=0.2, training=self.training, inplace=True)
        x2 = x1 + 1.0
        x3 = torch.nn.functional.dropout(x2, p=0.3)
        return x3

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.rand(1)
        x3 = torch.randint(0, 9, (1,))
        x4 = torch.rand_like(x3)
        x5 = torch.nn.functional.dropout(x1)
        x6 = torch.nn.functional.dropout(x2)
        x7 = torch.nn.functional.dropout(x3)
        return x7

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.rand(1)
        x3 = torch.randint(0, 9, (1,))
        x4 = torch.rand_like(x3)
        x5 = torch.nn.functional.dropout(x1)
        return x5



func = Model().to('cpu')


labels = torch.randn(1, 10, requires_grad=True)

x1 = torch.randn(1)

test_inputs = [labels, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''