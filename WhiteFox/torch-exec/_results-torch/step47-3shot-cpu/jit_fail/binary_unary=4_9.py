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

    def forward(self, x):
        t1 = x
        t2 = self.linear(t1, b=other)
        t3 = F.relu(t2)
        return t3


other = 1

func = Model(other).to('cpu')


x = torch.randn(1, 16)

test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear'

jit:
'Model' object has no attribute 'linear'
'''