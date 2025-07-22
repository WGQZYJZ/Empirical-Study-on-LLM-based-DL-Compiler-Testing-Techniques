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

    def forward(self, x1):
        v1 = x1.reshape(x1.shape[0], -1)
        v2 = torch.nn.functional.linear(v1, torch.eye(512, dtype=torch.float), bias=torch.zeros(512, dtype=torch.float))
        v3 = v2.flatten(start_dim=1)
        v4 = v3 + 3
        v5 = torch.clamp(v4, min=0)
        v6 = torch.clamp(v5, max=6)
        v7 = v6 / 6
        return v7


func = Model().to('cpu')


x1 = torch.randn(1, 100, 512)
x1 = torch.randn(1, 100, 512)
x1 = torch.randn(1, 100, 512)
v1 = x1.reshape(x1.shape[0], -1)

test_inputs = [x1, v1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''