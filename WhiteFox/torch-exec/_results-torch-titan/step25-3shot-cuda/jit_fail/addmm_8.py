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

    def forward(self, x, inp):
        v1 = torch.mm(x, x)
        v2 = (v1 + inp)
        return v2.transpose(0, 1)




func = Model().to('cuda')



v1 = torch.randn(60, 10, requires_grad=True)



v2 = torch.randn(60, 5, requires_grad=True)



inp = torch.randn(10)


test_inputs = [v1, v2, inp]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''