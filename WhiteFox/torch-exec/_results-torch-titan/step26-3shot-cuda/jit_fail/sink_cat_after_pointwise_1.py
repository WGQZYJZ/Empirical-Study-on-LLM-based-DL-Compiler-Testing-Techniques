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

    def forward(self, input):
        conv = nn.Conv1d(in_channels=1, out_channels=1, kernel_size=1, groups=2)
        batchnorm = nn.BatchNorm1d(2)
        relu = nn.ReLU()
        out = conv(input)
        out = batchnorm(out)
        out = out.view(out.shape[2], (- 1))
        out = out[:, :1]
        out = relu(out)
        return out




func = Model().to('cuda')



input = torch.randn(1, 1, 10)


test_inputs = [input]

# JIT_FAIL
'''
direct:
in_channels must be divisible by groups

jit:
in_channels must be divisible by groups
'''