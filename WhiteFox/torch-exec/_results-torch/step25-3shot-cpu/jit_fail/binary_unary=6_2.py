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
        self.linear = torch.nn.Linear(4, 6, bias=True)
        self.other = torch.Tensor([1.5])

    def forward(self, x1):
        v0 = x1.flatten(1)
        v1 = self.linear(v0)
        v2 = v1 - self.other
        v3 = relu(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'relu' is not defined

jit:
NameError: name 'relu' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''