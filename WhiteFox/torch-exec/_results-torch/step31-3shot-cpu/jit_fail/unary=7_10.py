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
        self.linear = torch.nn.Linear(64, 64, bias=False)

    def forward(self, x):
        v1 = self.act(x)
        v2 = v1 * torch.clamp(v1 + 3, 0, 6)
        return v2 / 6



func = Model().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'act'

jit:
'Model' object has no attribute 'act'
'''