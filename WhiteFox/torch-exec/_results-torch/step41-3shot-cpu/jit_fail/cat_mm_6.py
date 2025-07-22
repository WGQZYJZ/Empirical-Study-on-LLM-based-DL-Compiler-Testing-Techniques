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
        v.append(torch.mm(x1, x2))
        v.append(torch.mm(x1, x2))
        for loopVar1 in range(5):
            v.append(torch.mm(x1, x2))
            v.append(torch.mm(x1, x2))
            v.append(torch.mm(x1, x2))
        for loopVar2 in range(3):
            for loopVar3 in range(3):
                v.append(torch.mm(x1, x2))
                v.append(torch.mm(x1, x2))
                v.append(torch.mm(x1, x2))
        return torch.cat(v, 1)



func = Model().to('cpu')


x1 = torch.randn(5, 5)
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mm(): argument 'mat2' (position 2) must be Tensor, not int

jit:
mm(): argument 'mat2' (position 2) must be Tensor, not int
'''