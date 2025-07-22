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
        self.in_features = 4096
        self.out_features = 10
        self.weight = torch.nn.parameter.Parameter(torch.ones(self.in_features, self.out_features))

        def forward(self, x1):
            y = torch.matmul(x1, self.weight)
            y1 = y + y
            return torch.relu(y1)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Module [Model] is missing the required "forward" function

jit:
Module [Model] is missing the required "forward" function
'''