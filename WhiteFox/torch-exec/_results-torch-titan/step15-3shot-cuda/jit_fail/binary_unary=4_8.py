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

    def __init__(self, other_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=7, out_features=7)
        self.other_tensor = other_tensor

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.other_tensor)
        v3 = torch.nn.functional.relu(v2)
        return v3




other_tensor = torch.randn(7)

func = Model(other_tensor).to('cuda')



other_tensor = torch.randn(7)



x1 = torch.randn(1, 7)


test_inputs = [other_tensor, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''