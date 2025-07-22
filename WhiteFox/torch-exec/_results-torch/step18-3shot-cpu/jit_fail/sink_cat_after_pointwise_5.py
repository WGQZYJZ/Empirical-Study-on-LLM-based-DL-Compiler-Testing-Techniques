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

    def __init__(self, tch):
        super().__init__()
        self.tch = tch

    def forward(self, x):
        x = torch.cat((x, self.tch), dim=1) if x.shape != self.tch.shape else x
        y = torch.tanh(x.view(x.shape[0], -1))
        return y


tch = torch.randn(1, 6)

func = Model(tch).to('cpu')


x = torch.randn(2, 3, 4)

tch = torch.randn(1, 6)

test_inputs = [x, tch]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''