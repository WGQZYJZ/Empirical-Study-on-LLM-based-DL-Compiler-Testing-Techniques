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
        self.linear = torch.nn.Linear(8, 8)

    def forward(l1):
        v1 = self.linear(l1)
        v2 = (v1 + 3)
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = (v3 / 6)
        return v4



func = Model().to('cuda')



l1 = torch.randn(1, 8)


test_inputs = [l1]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''