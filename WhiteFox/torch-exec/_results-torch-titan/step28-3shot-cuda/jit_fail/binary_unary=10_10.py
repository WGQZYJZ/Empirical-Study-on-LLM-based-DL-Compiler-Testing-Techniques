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
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + input2)
        v3 = v2.relu()
        return v3



func = Model().to('cuda')



input2 = torch.randn(1, 2)



x1 = torch.randn(1, 2)


test_inputs = [input2, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''