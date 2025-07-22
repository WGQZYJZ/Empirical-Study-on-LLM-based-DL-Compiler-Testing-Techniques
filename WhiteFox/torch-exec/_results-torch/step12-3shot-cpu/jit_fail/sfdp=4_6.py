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

    def forward(self, x1, x2, x3, x4):
        q = torch.matmul(x1, x2)
        k = torch.matmul(x3, x4)
        v = k



func = Model().to('cpu')

x1 = 1
x2 = 1
x3 = 1
x4 = 1

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
matmul(): argument 'input' (position 1) must be Tensor, not int

jit:
matmul(): argument 'input' (position 1) must be Tensor, not int
'''