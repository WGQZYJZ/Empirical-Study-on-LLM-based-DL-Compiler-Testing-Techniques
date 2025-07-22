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

    def __init__(self, linear, bias):
        super().__init__()
        self.linear = linear
        self.bias = bias

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.bias
        return v2


linear = 1
bias = 1
func = Model(lin, b).to('cpu')



b = torch.nn.Parameter(torch.randn(64, 64))

x1 = torch.randn(1, 64)

test_inputs = [b, x1]
