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
        self.t = torch.nn.Transformer()

    def forward(self, v1):
        v2 = self.t(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 32, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
forward() missing 1 required positional argument: 'tgt'

jit:
forward() missing 1 required positional argument: 'tgt'
'''