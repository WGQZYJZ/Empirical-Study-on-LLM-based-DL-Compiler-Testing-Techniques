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
        self._weight = torch.nn.Parameter((torch.randn(1, ((2 * 3) * 4)) + 0.01))

    def forward(self, x):
        return (x * self._weight)




func = Model().to('cuda')



x = torch.randn(2, 3, 4)



w = torch.randn(2, 28)


test_inputs = [x, w]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''