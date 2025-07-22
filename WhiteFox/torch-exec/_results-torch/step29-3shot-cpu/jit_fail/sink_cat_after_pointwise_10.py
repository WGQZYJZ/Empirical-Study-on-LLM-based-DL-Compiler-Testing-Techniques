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

    def forward(self, x):
        y = torch.cat((x, x), dim=1)
        v1 = y.view(y.shape[0], -1) if torch.numel(v1) == 1 else v1.view(v1.shape[0], -1)
        v2 = v1.tanh()
        x = v2.tanh()
        return x



func = Model().to('cpu')


x = torch.randn(2, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
local variable 'v1' referenced before assignment

jit:
local variable 'v1' referenced before assignment
'''