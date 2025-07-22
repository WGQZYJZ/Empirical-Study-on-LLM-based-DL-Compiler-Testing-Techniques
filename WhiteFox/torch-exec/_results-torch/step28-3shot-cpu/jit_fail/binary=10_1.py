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
        self.linear = torch.nn.Linear(17, 10)
        self.linear.bias = torch.nn.Parameter(torch.tensor([0.909703, -0.011381, -0.037906, 1.987684, -1.719269, -0.758099, 0.418843, -0.735989, 1.524456, -1.688067]))
        self.linear.weight = torch.nn.Parameter(torch.tensor([-0.240726, -0.0442, -0.540115, -0.269951, -0.476428, 0.091757, -0.781907, -0.409872, 0.30332, -0.425438, 0.890566, 0.881638, 0.463365, -0.63876, 0.092376, 0.230328, -0.570235, -0.504842, -1.309621, -0.022977, 0.087456, 0.637414]))
        self.linear.weight.requires_grad = False

    def forward(self, input_tensor, other):
        return self.linear(input_tensor) + other


func = Model().to('cpu')


input_tensor = torch.randn(7, 17)

other = torch.randn(7, 10)

test_inputs = [input_tensor, other]

# JIT_FAIL
'''
direct:
mat2 must be a matrix, got 1-D tensor

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(7, 17)), Parameter(FakeTensor(..., size=(22,))), Parameter(FakeTensor(..., size=(10,), requires_grad=True))), **{}):
b must be 2D

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''