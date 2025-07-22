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
        self.conv_t = torch.nn.ConvTranspose2d(8, 1, 2)

    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

jit:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int
'''