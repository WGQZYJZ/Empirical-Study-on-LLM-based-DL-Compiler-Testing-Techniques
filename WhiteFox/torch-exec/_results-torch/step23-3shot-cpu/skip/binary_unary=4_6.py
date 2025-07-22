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

    def __init__(self, weight, bias):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
        self.linear.weight = weight
        self.linear.bias = bias

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 + x2
        v3 = torch.nn.functional.relu(v2)
        return v3


weight = torch.tensor([[1.0, 2.0]]).float()
bias = torch.tensor([3.0]).float()
func = Model(weight, bias).to('cpu')


weight = torch.tensor([[1.0, 2.0]]).float()

bias = torch.tensor([3.0]).float()

x1 = torch.tensor([[1.0, 2.0]]).float()

x2 = torch.tensor([3.0]).float()

test_inputs = [weight, bias, x1, x2]
