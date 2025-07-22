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
        self.linear1 = torch.nn.Linear(1, 5)
        self.linear2 = torch.nn.Linear(5, 1)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = (v1 + v2)



func = Model().to('cuda')



x1 = torch.randn(1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'v2' referenced before assignment

jit:
local variable 'v2' referenced before assignment
'''