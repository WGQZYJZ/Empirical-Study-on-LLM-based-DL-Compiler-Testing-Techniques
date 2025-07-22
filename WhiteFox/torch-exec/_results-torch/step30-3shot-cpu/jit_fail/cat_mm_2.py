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

    def forward(self, x1, x2):
        v = []
        v.append(x1)
        for i in range(5, 10):
            v.append(i)
        v.append(x2)
        return torch.cat(v, 1)



func = Model().to('cpu')


x1 = torch.randn(1, 2)

x2 = torch.randn(1, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
expected Tensor as element 1 in argument 0, but got int

jit:
expected Tensor as element 1 in argument 0, but got int
'''