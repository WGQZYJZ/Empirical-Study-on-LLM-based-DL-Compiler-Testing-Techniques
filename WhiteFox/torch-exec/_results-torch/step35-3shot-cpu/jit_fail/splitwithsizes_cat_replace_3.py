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
        self.features = torch.nn.ModuleList([torch.nn.Linear(1, 1)])
        self.feature0 = torch.nn.Linear(1, 1)
        self.feature1 = torch.nn.Linear(1, 1)

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=-7)
        return (split_tensors, concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-4, 3], but got -7)

jit:
Failed running call_function <built-in method cat of type object at 0x7370a7596ec0>(*((FakeTensor(..., size=(1, 1, 64, 64)), FakeTensor(..., size=(1, 1, 64, 64)), FakeTensor(..., size=(1, 1, 64, 64))),), **{'dim': -7}):
Dimension out of range (expected to be in range of [-4, 3], but got -7)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''