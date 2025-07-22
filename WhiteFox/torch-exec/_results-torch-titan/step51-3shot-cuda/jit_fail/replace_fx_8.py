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

    def __init__(self, p1):
        super().__init__()
        self.p1 = p1

    def forward(self, x1):
        x2 = (x1 + self.p1)
        x3 = torch.rand_like(x2)
        return x3




p1 = torch.tensor([2.0])


func = Model(p1).to('cuda')



p1 = torch.tensor([2.0])



x1 = torch.randn(6, 6)


test_inputs = [p1, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''