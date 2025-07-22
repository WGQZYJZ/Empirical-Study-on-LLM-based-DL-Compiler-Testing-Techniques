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

    def forward(self, x1, x2, *args, x4):
        v4 = torch.mm(x4, x4)
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x2, x2)
        return ((v1 + v2) + v4)




func = Model().to('cuda')



x1 = torch.randn(2, 2)



x2 = torch.randn(2, 2)



x3 = torch.randn(2, 2)



x4 = torch.randn(2, 2)



x5 = torch.randn(2, 2)



x6 = torch.randn(2, 2)



x7 = torch.randn(2, 2)


test_inputs = [x1, x2, x3, x4, x5, x6, x7]

# JIT_FAIL
'''
direct:
forward() missing 1 required keyword-only argument: 'x4'

jit:
forward() missing 1 required keyword-only argument: 'x4'
'''