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

    def forward(self, x):
        return torch.clamp_max(self.leaky_relu(torch.mean(torch.abs(x), dim=(2, 3), keepdim=True)), max=1.3)



func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'leaky_relu'

jit:
'Model' object has no attribute 'leaky_relu'
'''