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

    def __init__(self, input_size: int, output_size: int):
        super().__init__()
        self.linear = torch.nn.Linear(input_size, output_size)

    def forward(self, t1, t2):
        v1 = self.linear(t1)
        v2 = (v1 - v2)
        return v2



input_size = 1
output_size = 1
func = Model(10, 5).to('cuda')



t1 = torch.randn(5, 10)



t2 = torch.randn(5, 10)


test_inputs = [t1, t2]

# JIT_FAIL
'''
direct:
local variable 'v2' referenced before assignment

jit:
local variable 'v2' referenced before assignment
'''