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

    def __init__(self, weight):
        super().__init__()
        self.linear = torch.nn.Linear(8, 8)
        self.linear.weight.data = torch.Tensor([weight], requires_grad=True)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 + x2
        v3 = F.relu(v2)
        return v3


weight = 1
func = Model(1.0).to('cpu')


x1 = torch.randn(1, 8)

x2 = torch.randn(1, 8)

test_inputs = [x1, x2]
