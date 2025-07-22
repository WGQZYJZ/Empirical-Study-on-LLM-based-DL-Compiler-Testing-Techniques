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
        self.linear = torch.nn.Linear(4, 8, bias=False)
        self.linear.weight = torch.nn.Parameter(torch.zeros((8, 4)))
        for i in range(4):
            self.linear.weight[i, i] = 1

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + some_tensor
        v3 = F.relu(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 4)

test_inputs = [x1]
