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

    def __init__(self, negative_slope=0.01):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(64, 128)
        self.negative_slope = torch.nn.parameter.Parameter(torch.tensor(negative_slope))

    def forward(self, x1):
        v1 = torch.nn.functional.leaky_relu(self.linear(x1), negative_slope=self.negative_slope)
        return v1



func = Model().to('cuda')



x1 = torch.randn(8, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
leaky_relu(): argument 'negative_slope' (position 2) must be Number, not Parameter

jit:
Failed running call_function <function leaky_relu at 0x7345d6ea10d0>(*(FakeTensor(..., device='cuda:0', size=(8, 128)),), **{'negative_slope': Parameter(FakeTensor(..., device='cuda:0', size=(), requires_grad=True))}):
leaky_relu(): argument 'negative_slope' (position 2) must be Number, not FakeTensor

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''