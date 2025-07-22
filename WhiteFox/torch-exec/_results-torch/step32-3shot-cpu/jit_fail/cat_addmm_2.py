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
        self.layers = nn.Linear(2, 5)

    def forward(self, x):
        x = torch.addmm(x, self.layers, self.layers)
        x = torch.cat((x, x), dim=1)
        x = torch.stack((x, x, x), dim=1)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
addmm(): argument 'mat1' (position 2) must be Tensor, not Linear

jit:
addmm(): argument 'mat1' (position 2) must be Tensor, not Linear
'''