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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 5, 1, 2), torch.nn.Conv2d(32, 32, 3, 2, 1))
        self.cat = torch.nn.Sequential(torch.nn.Sigmoid())

    def forward(self, x0):
        split_tensor = torch.split(x0, 6, dim=3)
        split_tensors = [torch.stack(tensors, dim=0) for tensors in zip(*split_tensor)]
        concatenated_tensor = torch.cat(split_tensors, 3)
        return (concatenated_tensor, torch.split(x0, 6, dim=3))



func = Model().to('cpu')


x0 = torch.randn(3, 64, 1, 128)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
stack expects each tensor to be equal size, but got [64, 1, 6] at entry 0 and [64, 1, 2] at entry 21

jit:
Failed running call_function <built-in method stack of type object at 0x7d02eb396ec0>(*((FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 6)), FakeTensor(..., size=(64, 1, 2))),), **{'dim': 0}):
stack expects each tensor to be equal size, but got torch.Size([64, 1, 6]) at entry 0 and torch.Size([64, 1, 2]) at entry 21

from user code:
   File "<string>", line 22, in forward
  File "<string>", line 22, in <listcomp>


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''