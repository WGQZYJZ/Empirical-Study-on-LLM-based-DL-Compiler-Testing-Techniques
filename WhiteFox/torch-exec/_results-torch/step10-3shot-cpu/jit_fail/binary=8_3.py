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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1, groups=1)

    def forward(self, tensor, x2):
        return self.conv(tensor, x2=x2)


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 16, 16)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'x2'

jit:
forward() got an unexpected keyword argument 'x2'
'''