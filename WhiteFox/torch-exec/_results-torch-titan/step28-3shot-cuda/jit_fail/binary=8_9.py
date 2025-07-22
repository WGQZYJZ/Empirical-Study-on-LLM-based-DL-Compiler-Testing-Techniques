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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, t2):
        v1 = self.conv(x1)
        v6 = (v6 + t2)
        return v6



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



t2 = torch.randn(1, 8, 64, 64)


test_inputs = [x1, t2]

# JIT_FAIL
'''
direct:
local variable 'v6' referenced before assignment

jit:
local variable 'v6' referenced before assignment
'''