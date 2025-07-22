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
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.clamp_min(v1, (- 12.0))
        v3 = torch.clamp_max(v2, 12.0)
        return v3



func = Model().to('cuda')



x = torch.randn(1, 8, 32, 32)



min_value = torch.tensor((- 12.0))



max_value = torch.tensor(12.0)


test_inputs = [x, min_value, max_value]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''