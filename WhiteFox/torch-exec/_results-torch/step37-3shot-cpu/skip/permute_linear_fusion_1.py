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
        self.linear = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v2 = torch.sign(v2)
        v3 = torch.min(v2, dim=-1)[1]
        x2 = torch.min(v3, dim=-1)[1]
        x3 = x2.unsqueeze(dim=-1)
        v3 = v3 + x3.to(v3.dtype)
        v3 = torch.mean(v3.T)
        return (v1[0][0] == v3.item()).to(torch.float32)

class Model(torch.nn.Module):

    def __init__(self):
        pass

    def forward(self):
        m = torch.nn.Softmax()
        return m.weight



func = Model().to('cpu')


x1 = torch.randn(2, 2, 3)

test_inputs = [x1]
