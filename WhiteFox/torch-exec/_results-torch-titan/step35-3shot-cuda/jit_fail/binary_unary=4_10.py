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
        self.linear = torch.nn.Linear(12, 10, bias=True)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = (v1 + other)
        v3 = v2.relu()
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 12)



kw_other_1 = torch.randn(1, 10)



kw_other_2 = torch.randn(10)


test_inputs = [x1, kw_other_1, kw_other_2]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''