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

class SinkCat(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = torch.cat((x, torch.nn.ReLU(x)), dim=1).view(x.shape[0], -1)
        x = torch.tanh(x)
        return x



func = SinkCat().to('cpu')


x = torch.randn(3, 2, requires_grad=True)

test_inputs = [x]

# JIT_FAIL
'''
direct:
expected Tensor as element 1 in argument 0, but got ReLU

jit:
expected Tensor as element 1 in argument 0, but got ReLU
'''