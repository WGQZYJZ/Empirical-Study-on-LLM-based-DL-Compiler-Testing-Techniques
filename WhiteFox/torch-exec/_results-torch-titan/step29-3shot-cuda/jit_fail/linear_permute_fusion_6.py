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
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x1):
        v1 = torch.nn.functional.interpolate(x1, scale_factor=(1.0, 1.0), mode='nearest')
        v2 = v1.permute(0, 2, 3, 1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 4, 4, 4)


x1 = torch.randn(1, 4, 4, 4)


x2 = x1.squeeze(0)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''