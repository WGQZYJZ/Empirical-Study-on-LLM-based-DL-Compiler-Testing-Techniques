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
        self.conv = torch.nn.Conv2d(3, 64, (3, 3))
        self.bn = torch.nn.BatchNorm2d(64)

    def forward(self, x):
        a1 = self.bn(self.conv(x))
        n1 = torch.flatten(a1, 1)
        a2 = self.linear(n1)
        v1 = torch.transpose(a2, 0, 1)
        v2 = a2 - n1
        return n1


func = Model().to('cuda')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear'

jit:
'Model' object has no attribute 'linear'
'''