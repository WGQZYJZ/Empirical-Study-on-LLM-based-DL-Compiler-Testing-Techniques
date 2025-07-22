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
        self.linear = torch.nn.Linear(10, 64)

    def forward(self, x1):
        v1 = self.linear(x1)
        _ = self.__call__.clamp(v1, min_value=5.0, max_value=6.0)



func = Model().to('cuda')



x1 = torch.randn(1, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'function' object has no attribute 'clamp'

jit:
'function' object has no attribute 'clamp'
'''