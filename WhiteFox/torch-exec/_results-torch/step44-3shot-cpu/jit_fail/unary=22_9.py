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
        self.linear1 = torch.nn.Linear(3, 8, bias=True)
        self.bn1 = torch.nn.BatchNorm2d(8)

    def forward(self, x1):
        v1 = self.bn1(self.linear1(x1))
        v2 = v1.tanh()
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected 4D input (got 2D input)

jit:
expected 4D input (got 2D input)
'''