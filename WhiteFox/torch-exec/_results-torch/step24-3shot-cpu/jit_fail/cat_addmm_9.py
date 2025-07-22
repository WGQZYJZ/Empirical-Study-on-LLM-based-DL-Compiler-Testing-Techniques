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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 2)

    def forward(self, x):
        x = self.layers(x)
        x = torch.tensor(x)
        x = torch.stack((x, x, x), dim=1)
        x = x.flatten(start_dim=1)
        return x



func = Model().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''