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

    def forward(self, x1, x2, inp):
        v1 = torch.mm(x2, inp)
        v2 = v1 * torch.sigmoid(x1)
        return v2



func = Model().to('cpu')

x1 = 1
x2 = 1
inp = 1

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mm(): argument 'input' (position 1) must be Tensor, not int

jit:
mm(): argument 'input' (position 1) must be Tensor, not int
'''