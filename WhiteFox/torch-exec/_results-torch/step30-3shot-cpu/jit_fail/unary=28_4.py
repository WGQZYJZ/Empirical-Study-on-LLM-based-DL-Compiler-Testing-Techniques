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
        self.fc = torch.nn.Linear(64, 10)

    def forward(self, x1, **kwargs):
        v1 = self.fc(x1)
        v2 = torch.clamp_min(v1, max(kwargs['min_value'], v2.min()))
        v3 = torch.clamp_max(v2, kwargs['max_value'])
        return v3


func = Model().to('cpu')


x1 = torch.randn(64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'min_value'

jit:
'min_value'
'''