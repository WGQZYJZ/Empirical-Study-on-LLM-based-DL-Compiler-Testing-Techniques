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
        self.fc = torch.nn.Linear(25088, 1000)

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 + input_1
        v3 = torch.relu(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 25088)

input_1 = torch.randn(1, 1000)

test_inputs = [x1, input_1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''