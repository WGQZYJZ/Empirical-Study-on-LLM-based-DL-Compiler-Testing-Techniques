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

    def forward(self, x1):
        v1 = x1
        v3 = x1.shape
        v2 = torch.nn.functional.linear(v1, v3, v3, True)
        v3 = v2.permute(0, 2, 1)
        return v3



func = Model().to('cpu')


x1 = torch.randn(4, 3, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear() takes from 2 to 3 positional arguments but 4 were given

jit:
linear() takes from 2 to 3 positional arguments but 4 were given
'''