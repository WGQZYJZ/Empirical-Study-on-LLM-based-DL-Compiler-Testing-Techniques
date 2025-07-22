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
        self.query = torch.nn.Parameter(torch.rand(2048, 1024))
        self.key = torch.nn.Parameter(torch.rand(1024, 1024))
        self.value = torch.nn.Parameter(torch.rand(1024, 1024))
        self.dropout_p = 0.1
        self.scale_factor = 1024 ** (-0.5)

    def forward(self, x1):
        v1 = torch.matmul(x2, self.key.transpose(-2, -1))
        v2 = v1.div(self.scale_factor)
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=self.dropout_p)
        v5 = self.value.matmul(v4)
        return v5


func = Model().to('cpu')


x1 = torch.randn(1, 2048, 1024)

x2 = torch.randn(1, 2048, 1024)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''