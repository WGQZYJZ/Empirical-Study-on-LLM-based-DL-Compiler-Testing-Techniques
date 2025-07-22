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

    def __init__(self, linear_weight, linear_bias, relu_weight, relu_bias):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(3, 4)
        self.relu = torch.nn.ReLU()
        self.linear.weight = torch.nn.Parameter(linear_weight)
        self.linear.bias = torch.nn.Parameter(linear_bias)
        self.relu.weight = torch.nn.Parameter(relu_weight)
        self.relu.bias = torch.nn.Parameter(relu_bias)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + other)
        v3 = self.relu(v2)
        v4 = self.relu(v3)
        return v4



linear_weight = 1
linear_bias = 1
relu_weight = 1
relu_bias = 1

func = Model(linear_weight, linear_bias, relu_weight, relu_bias).to('cuda')

x1 = 1

test_inputs = [x1]
