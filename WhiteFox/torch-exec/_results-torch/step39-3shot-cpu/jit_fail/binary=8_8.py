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

    def forward(self, x1, x2):
        x1 = self.conv1(x1)
        x2 = self.conv2(x2)
        v1 = x1
        v2 = x2
        v3 = v1 + v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv1'

jit:
'Model' object has no attribute 'conv1'
'''