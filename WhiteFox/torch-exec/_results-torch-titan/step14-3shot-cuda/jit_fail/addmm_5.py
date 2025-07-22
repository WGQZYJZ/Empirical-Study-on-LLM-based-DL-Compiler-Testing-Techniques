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

    def forward(self, matrix):
        v1 = torch.mm(matrix, torch.tensor(2.0))
        return v1




func = Model().to('cuda')



matrix = torch.randn(5, 5)



inp1 = torch.randn(1, 1)



inp2 = torch.randn(1, 1)


test_inputs = [matrix, inp1, inp2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''