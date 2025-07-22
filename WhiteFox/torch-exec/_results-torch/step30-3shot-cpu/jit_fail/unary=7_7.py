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

    def __init__(self, in_channels, out_features):
        super().__init__()
        self.linear = torch.nn.Linear(in_channels, out_features)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * torch.clamp(torch.min(v1), min=0.0, max=6.0)
        v3 = v2 / 6
        return v3


in_channels = 1
out_features = 1

func = Model(in_channels, out_features).to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''