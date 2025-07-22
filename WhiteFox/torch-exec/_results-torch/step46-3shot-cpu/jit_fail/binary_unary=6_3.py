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
        self.linear = torch.nn.Linear(28 ** 2, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 5
        v3 = self.activation_fun(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 28 ** 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'activation_fun'

jit:
'Model' object has no attribute 'activation_fun'
'''