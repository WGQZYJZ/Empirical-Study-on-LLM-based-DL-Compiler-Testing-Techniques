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
        self.linear = torch.nn.Linear(64, 32)

    def forward(self, x1, x2=None):
        if (not x2):
            return self.linear(x2)
        o = self.linear(x1)
        o += x2
        return torch.nn.functional.relu(o)



func = Model().to('cuda')



x1 = torch.randn(1, 64)



x2 = torch.randn(1, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
Boolean value of Tensor with more than one value is ambiguous
'''