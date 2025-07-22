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

    def __init__(self, D_key, D_val, N, D_model, H, D_inner):
        super().__init__()
        self.linear = torch.nn.Linear(D_model, H)
        self.linear.weight.data.normal_(mean=0, std=1)
        self.linear.bias.data.zero_()
        self.scale_factor = np.sqrt(D_key)
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, x1, x2, x3):
        x1 = self.linear(x1)
        x2 = x2 * self.scale_factor
        x3 = x3.transpose(-2, -1)
        v1 = torch.matmul(x1, x2)
        v2 = v1.mul(self.scale_factor).softmax(dim=-1)
        v3 = self.dropout(v2)
        out = torch.matmul(x3, v3)
        return out


D_key = 1
D_val = 1
N = 1
D_model = 1
H = 1
D_inner = 1

func = Model(D_key, D_val, N, D_model, H, D_inner).to('cpu')

x1 = 1
x2 = 1
x3 = 1

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''