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

class SinkCat(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = (x, x, x).pop()
        y = (x, x, x).pop()
        z = y + 10
        x = z * 2 + 3
        x = x.tanh()
        return x



func = SinkCat().to('cpu')


x = torch.randn(2, requires_grad=True)

test_inputs = [x]

# JIT_FAIL
'''
direct:
'tuple' object has no attribute 'pop'

jit:
'tuple' object has no attribute 'pop'
'''