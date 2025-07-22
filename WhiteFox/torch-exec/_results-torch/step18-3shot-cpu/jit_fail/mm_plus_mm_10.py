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
        super(Model, self).__init__()
        self.linear_1 = nn.Linear(32, 32)
        self.relu_1 = nn.ReLU()
        self.t5 = nn.Linear(64, 10)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.linear_1(x)
        x = self.relu_1(x)
        x = self.t5(x)
        x = self.softmax(x)
        return x



func = Model().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''