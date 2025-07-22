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

    def __init__(self, min_value=0.01, max_value=0.5):
        super().__init__()
        self.linear = torch.nn.Linear(128, 32)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=self.min_value)
        v3 = torch.clamp_max(v2, max_value=self.max_value)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'min_value'

jit:
'Model' object has no attribute 'min_value'
'''