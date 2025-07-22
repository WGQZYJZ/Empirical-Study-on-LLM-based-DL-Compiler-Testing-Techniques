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
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x1, x2, other):
        v1 = self.lineair(x1)
        v2 = v1 + x2
        return v2


func = Model().to('cpu')


x1 = torch.randn(20, 10)

x2 = torch.randn(20, 10)

other = torch.randn(20, 10)

test_inputs = [x1, x2, other]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'lineair'

jit:
'Model' object has no attribute 'lineair'
'''