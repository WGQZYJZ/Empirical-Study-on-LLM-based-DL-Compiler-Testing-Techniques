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

class Layer1(torch.nn.Module):

    def __init__(self, inp, hidden, out):
        super().__init__()
        self.op1 = torch.nn.Sequential(torch.nn.ReLU(True), torch.nn.Conv2d(inp, hidden, 1, 1, 0, bias=False))
        self.op2 = torch.nn.Sequential(torch.nn.AdaptiveAvgPool2d(1), torch.nn.Linear(hidden, out, bias=True))

    def forward(self, v1):
        return self.op2(self.op1(v1))

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.features = Layer1(32, 16, 64)

    def forward(self, x):
        split_tensors = torch.split(x, [1, 1, 1], dim=-1)
        concatenated_tensor = torch.cat(split_tensors, dim=-1)
        return (concatenated_tensor.reshape((concatenated_tensor.shape[0], -1)), torch.split(x, [1, 1, 1], dim=-1))



func = Model().to('cpu')


x = torch.randn(2, 32, 10, 10)

test_inputs = [x]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 10 (input tensor's size at dimension -1), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x7c8a7ed7bf70>(*(FakeTensor(..., size=(2, 32, 10, 10)), [1, 1, 1]), **{'dim': -1}):
Split sizes add up to 3 but got the tensor's size of 10

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''