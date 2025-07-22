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
        self.fc1 = torch.nn.Linear(2304, 1152)
        self.fc2 = torch.nn.Linear(1152, 1152)
        self.fc3 = torch.nn.Linear(1152, 1152)
        self.fc4 = torch.nn.Linear(1152, 1152)
        self.fc5 = torch.nn.Linear(1152, 1152)
        self.fc6 = torch.nn.Linear(1152, 1152)
        self.fc7 = torch.nn.Linear(1152, 1152)
        self.fc8 = torch.nn.Linear(1152, 1152)
        self.fc9 = torch.nn.Linear(1152, 1152)

    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = self.fc2(v1)
        v3 = self.fc3(v2)
        v4 = self.fc4(torch.cat([v2, v3], dim=1))
        v5 = self.fc5(v4)
        v6 = self.fc6(v5)
        v7 = self.fc7(v6)
        v8 = self.fc8(v7)
        v9 = self.fc9(torch.cat([v2, v3, v4, v5, v6, v7, v8], dim=1))
        return v9


func = Model().to('cpu')


x1 = torch.randn(1, 2304)

x2 = torch.randn(1, 2304)
x2 = torch.randn(1, 2304)
x1 = torch.randn(1, 2304)

x = torch.cat([x1, x2], dim=1)

test_inputs = [x1, x2, x]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''