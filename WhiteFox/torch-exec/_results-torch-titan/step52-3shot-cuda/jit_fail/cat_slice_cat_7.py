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

    def forward(self, x):
        a = torch.cat(x)
        b = a[:, 0:9223372036854775807]
        c = b[:, 0:0]
        return torch.cat([a, c])



func = Model().to('cuda')



x1 = torch.randn(4, 3)



x2 = torch.randn(3, 4)



x3 = torch.randn(4)



x4 = torch.randn(5)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''