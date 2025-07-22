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



class Model(nn.Module):

    def __init__(self, weight):
        super().__init__()
        self.layers = nn.Linear(1, 9, bias=False)
        self.weight = weight

    def forward(self, x):
        x = self.layers(x)
        x = torch.mm(x, self.weight)
        return x




weight = torch.randn((9, 3))


func = Model(weight).to('cuda')



x = torch.randn(3, 3)



weight = torch.randn((9, 3))


test_inputs = [x, weight]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''