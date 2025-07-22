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
        self.layer1 = None

    def forward(self, x1):
        v1 = self.layer1(x1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 20, 50, 75)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'NoneType' object is not callable

jit:
'NoneType' object is not callable
'''