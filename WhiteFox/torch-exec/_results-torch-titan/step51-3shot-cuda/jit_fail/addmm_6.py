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

    def forward(self, x1, x2, x4, x5, inp):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x4, x5)
        v3 = torch.mm(v1, v2)
        v4 = (v3 + inp)
        return v4




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 3)



x3 = torch.randn(3, 3, requires_grad=False)



x4 = torch.randn(3, 3, requires_grad=False)



x5 = torch.randn(3, 3)



inp = torch.randn(3, 3, 3)


test_inputs = [x1, x2, x3, x4, x5, inp]

# JIT_FAIL
'''
direct:
forward() takes 6 positional arguments but 7 were given

jit:
forward() takes 6 positional arguments but 7 were given
'''