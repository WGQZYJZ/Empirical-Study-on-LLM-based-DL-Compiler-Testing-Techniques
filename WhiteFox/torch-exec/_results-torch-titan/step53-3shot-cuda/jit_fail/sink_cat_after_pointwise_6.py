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

    def forward(self, x, y):
        z = torch.cat([x, y], dim=(- 1))
        z = z.view(([(- 1)] + list(z.shape[(z.dim() - 2):])))
        return z.relu()




func = Model().to('cuda')



x = torch.randn(2, 3)



y = torch.randn(2, 4)



z = torch.randn(2, 2, 3)



a = torch.randn(3, 2)


test_inputs = [x, y, z, a]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 5 were given

jit:
forward() takes 3 positional arguments but 5 were given
'''