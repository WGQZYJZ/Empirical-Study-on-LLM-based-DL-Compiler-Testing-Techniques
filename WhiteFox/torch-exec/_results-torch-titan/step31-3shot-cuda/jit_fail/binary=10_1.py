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

    def __init__(self, a):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
        self.a = a

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.a)
        return v2




a = torch.nn.Parameter(torch.randn(8), requires_grad=True)

func = Model(a).to('cuda')




a = torch.nn.Parameter(torch.randn(8), requires_grad=True)



x1 = torch.randn(4)


test_inputs = [a, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''