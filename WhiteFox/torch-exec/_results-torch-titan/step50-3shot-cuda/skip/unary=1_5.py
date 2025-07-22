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
        self.linear = Linear(5, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 + (((v1 * v1) * v1) * 0.044715))
        v4 = (v3 * 0.7978845608028654)
        v5 = torch.tanh(v4)
        v6 = (v5 + 1)
        v7 = (v2 * v6)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 5)



x2 = torch.randn(1, 5)



x3 = torch.randn(1, 5)



x4 = torch.randn(1, 5)



x5 = torch.randn(1, 5)



x6 = torch.randn(1, 5)



x7 = torch.randn(1, 5)



x8 = torch.randn(1, 5)



x9 = torch.randn(1, 5)


test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
