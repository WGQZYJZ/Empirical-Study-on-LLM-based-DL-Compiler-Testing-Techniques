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

    def forward(self, x1, x2, inp1, inp2):
        v1 = torch.mm(x1, x1)
        v2 = (v1 + inp1)
        v3 = (v2 + inp2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 3, requires_grad=True)



inp = torch.randn(3, 3, 3, requires_grad=True)



inp1 = torch.randn(3, 3, 3, requires_grad=True)



inp2 = torch.randn(3, 3, 3, requires_grad=True)


test_inputs = [x1, x2, inp, inp1, inp2]

# JIT_FAIL
'''
direct:
forward() takes 5 positional arguments but 6 were given

jit:
forward() takes 5 positional arguments but 6 were given
'''