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

    def __init__(self, in_features, out_features, bias):
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features, bias)
        self.linear.bias.data.copy_(torch.rand_like(self.linear.bias))

    def forward(self, x):
        v = self.linear(x)
        v_sub = v - self.linear.bias
        return (v, v_sub)


in_features = 1
out_features = 1
bias = 1
func = Model(32, hidden_units, True).to('cpu')


x = torch.randn(1, 32)

test_inputs = [x]
