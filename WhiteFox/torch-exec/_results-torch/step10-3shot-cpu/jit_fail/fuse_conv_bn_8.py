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

    def forward(self, x):
        output = F.conv2d(F.batch_norm(x))



func = Model().to('cpu')


x = torch.randn(1024, 2, 7, 7)

test_inputs = [x]

# JIT_FAIL
'''
direct:
batch_norm() missing 2 required positional arguments: 'running_mean' and 'running_var'

jit:
batch_norm() missing 2 required positional arguments: 'running_mean' and 'running_var'
'''