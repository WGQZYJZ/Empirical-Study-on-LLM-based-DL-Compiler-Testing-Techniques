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
        self.fc3 = torch.nn.Linear(28 * 28, 30)
        self.relu = torch.nn.ReLU()

    def forward(self, x2):
        v1 = self.fc3(x2)
        v2 = self.relu(v1)
        return v2


func = Model().to('cpu')

x2 = 1

test_inputs = [x2]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''