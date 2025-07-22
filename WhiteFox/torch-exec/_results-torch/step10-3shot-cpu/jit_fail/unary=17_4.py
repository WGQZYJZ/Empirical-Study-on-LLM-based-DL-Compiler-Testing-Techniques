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
        self.conv_1 = torch.nn.ConvTranspose2d(3, 3, 2, stride=2)
        self.conv_1.padding_mode = 'replicate'

    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = torch.relu(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Only `zeros` padding mode is supported for ConvTranspose2d

jit:
Only `zeros` padding mode is supported for ConvTranspose2d
'''