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
        self.conv1 = torch.nn.Conv2d(3, 32, 3, 1, 1)
        self.conv2 = torch.nn.Conv2d(32, 32, 3, 1, 1)
        self.conv3 = torch.nn.Conv2d(32, 32, 3, 1, 1)

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        split_tensors = torch.split(v2, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        split_tensors = torch.split(v3, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))



func = Model().to('cpu')


t1 = torch.randn(1, 3, 64, 64)

t2 = torch.randn(1, 2, 64, 64)

t3 = torch.randn(1, 3, 64, 64)

x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

x3 = torch.randn(1, 3, 64, 64)

test_inputs = [t1, t2, t3, x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 7 were given

jit:
forward() takes 2 positional arguments but 7 were given
'''