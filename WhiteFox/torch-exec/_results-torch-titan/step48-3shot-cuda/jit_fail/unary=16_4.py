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
        self.linear = torch.nn.Linear(3, 16)

    def forward(input):
        v1 = self.linear(x1)
        v2 = v1.relu()
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''