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
        self.conv1 = conv1 = torch.nn.Conv2d(3, 2, 3)
        self.fc1 = fc1 = torch.nn.Linear(16, 8)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        out = self.relu(self.conv1(x))
        out = out.view(out.size(0), -1)
        out = self.relu(self.fc1(out))
        return out



func = Model().to('cpu')


tensor1 = torch.randn(2, 3, 16, 16)

tensor2 = torch.randn(2, 3, 16, 16)

test_inputs = [tensor1, tensor2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''