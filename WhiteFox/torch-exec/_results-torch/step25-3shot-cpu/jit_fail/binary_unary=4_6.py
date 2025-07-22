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
        self.linear = torch.nn.Linear(5, 8)

    def forward(self, x1, x2=None):
        v1 = self.conv(x1)
        if x2 is None:
            x2 = torch.randn(1, 5, 64, 64)
        v2 = linear(v1, x2)
        v3 = torch.relu(v1)
        return v3


func = Model().to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv'

jit:
'Model' object has no attribute 'conv'
'''