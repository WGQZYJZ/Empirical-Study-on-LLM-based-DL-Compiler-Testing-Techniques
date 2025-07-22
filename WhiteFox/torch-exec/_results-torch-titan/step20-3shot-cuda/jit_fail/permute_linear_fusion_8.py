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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.sigmoid(torch.nn.Softplus(self.linear(x1)))
        return torch.cos(v1)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
sigmoid(): argument 'input' (position 1) must be Tensor, not Softplus

jit:
sigmoid(): argument 'input' (position 1) must be Tensor, not Softplus
'''