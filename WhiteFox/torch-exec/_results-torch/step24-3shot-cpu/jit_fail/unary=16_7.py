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
        self.linear2 = torch.nn.Linear(1000, 10)

    def forward(self, t1):
        v1 = self.linear(t1)
        v2 = torch.nn.ReLU()(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1000)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear'

jit:
'Model' object has no attribute 'linear'
'''