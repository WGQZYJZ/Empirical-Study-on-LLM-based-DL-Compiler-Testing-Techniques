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

    def __init__(self, weight, bias, scale):
        super().__init__()
        self.linear = torch.nn.Linear(32, 32)
        weight = weight.reshape(32, 32)
        bias = bias.reshape(32)
        scale = scale.reshape(1)
        weight = weight * scale[0]
        self.linear.weight.data = weight
        self.linear.bias.data = bias

    def forward(self, x1):
        return self.linear(x1)


weight = 1
bias = 1
scale = 1
func = Model([1.0, 2.0, 3.0], [-1.0, -2.0, -3.0], [20.0]).to('cpu')


x1 = torch.randn(1, 32)

test_inputs = [x1]
