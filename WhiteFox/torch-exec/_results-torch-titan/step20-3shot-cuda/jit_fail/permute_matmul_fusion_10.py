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
        v1 = x1.permute(0, 2, 1)
        v2 = input_tensor
        v3 = torch.bmm(v1, v2)
        v4 = torch.bmm(v2, v1)
        v5 = v3.permute(0, 2, 1)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)



x3 = torch.randn(1, 2, 2)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''