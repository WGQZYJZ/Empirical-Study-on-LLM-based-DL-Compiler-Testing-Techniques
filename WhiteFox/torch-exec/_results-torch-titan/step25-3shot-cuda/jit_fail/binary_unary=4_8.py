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

    def __init__(self, weight):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.weight = weight

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.weight)
        return torch.relu(v2)




weight = torch.randn(8, 3)

func = Model(weight).to('cuda')



weight = torch.randn(8, 3)



x1 = torch.randn(8, 3)


test_inputs = [weight, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''