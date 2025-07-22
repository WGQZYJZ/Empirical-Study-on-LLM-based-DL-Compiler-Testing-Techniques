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
        self.fc = torch.nn.Linear(8, 8)

    def forward(self, x1, **kwargs):
        v1 = self.fc(x1, **kwargs)
        v2 = v1 + kwargs['other']
        v3 = torch.relu(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 8)

other = torch.randn(1, 8)

test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''