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
        self.gru1 = torch.nn.LSTM(1, 1, 1)
        self.gru2 = torch.nn.LSTM(1, 1, 1)
        self.gru3 = torch.nn.LSTM(1, 1, 1)

    def forward(self, x1, x2):
        y1 = self.gru1(x1)
        y2 = self.gru2(y1)
        y3 = self.gru3(y2)
        z1 = torch.rand_like(y3[0])
        return z1[0]



func = Model().to('cpu')


x1 = torch.randn(1, 1, 1)

x2 = torch.randn(1, 1, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
'tuple' object has no attribute 'dim'

jit:
'tuple' object has no attribute 'dim'
'''