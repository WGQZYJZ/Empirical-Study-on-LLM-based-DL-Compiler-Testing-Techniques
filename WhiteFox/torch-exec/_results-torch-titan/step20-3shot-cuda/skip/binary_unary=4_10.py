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

    def __init__(self, linear_weight: torch.Tensor, linear_bias: torch.Tensor, other: torch.Tensor):
        super().__init__()
        self.linear = torch.nn.Linear(other.shape[1], 1)
        self.linear.weight.data = copy.deepcopy(linear_weight)
        self.linear.bias.data = copy.deepcopy(linear_bias)

    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = (v1 + other)
        v3 = torch.relu(v2)
        return v3




linear_weight = torch.randn(*m.linear.weight.data.shape)


linear_bias = torch.zeros(*m.linear.bias.data.shape)


other = torch.randn(1, *m.linear.weight.data.shape[1:])

func = Model(linear_weight, linear_bias, other).to('cuda')

x2 = 1

test_inputs = [x2]
