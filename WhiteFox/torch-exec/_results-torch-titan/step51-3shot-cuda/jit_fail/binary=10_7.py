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
        self.linear = torch.nn.Linear(64, 16384)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + __other__)
        return v2



func = Model().to('cuda')



__x1__ = torch.randn(1, 64)



__other__ = torch.randn(1, 16384)


test_inputs = [__x1__, __other__]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''