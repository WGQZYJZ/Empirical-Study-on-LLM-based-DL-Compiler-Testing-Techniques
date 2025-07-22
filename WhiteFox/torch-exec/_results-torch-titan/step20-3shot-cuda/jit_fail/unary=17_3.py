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
        self.t1 = torch.nn.ConvTranspose2d(3, 32, 3, stride=2, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose3d(32, 32, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.t1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv_transpose(v2)
        v4 = torch.tanh(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 128)



x2 = torch.randn(1, 3, 128, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''