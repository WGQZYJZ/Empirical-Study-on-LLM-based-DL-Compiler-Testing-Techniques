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
        v1 = (inp + torch.mm(x1, x2))
        return v1




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 3)



inp = torch.randn(3, 3)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''