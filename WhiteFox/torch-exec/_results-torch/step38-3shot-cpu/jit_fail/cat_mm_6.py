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
        self.x1 = torch.rand(1, 1)

    def forward(self, x2):
        v1 = torch.cat([torch.mm(self.x1, x2), torch.mm(self.x1, x2)], 1)
        return torch.cat([torch.mm(self.x1, x2), v1], 1)



func = Model().to('cpu')


x1 = torch.randn(3, 4)

x2 = torch.randn(4, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''