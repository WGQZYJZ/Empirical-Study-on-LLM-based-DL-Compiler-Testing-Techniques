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
        self.layers = torch.nn.ModuleList([])

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        for _ in range(4):
            self.layers.append(v1)
        return torch.cat(self.layers, 1)



func = Model().to('cpu')


x1 = torch.randn(2, 2)

x2 = torch.randn(2, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
torch.FloatTensor is not a Module subclass

jit:
torch.FloatTensor is not a Module subclass
'''