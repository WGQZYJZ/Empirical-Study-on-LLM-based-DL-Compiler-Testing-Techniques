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

    def forward(self, x1):
        v2 = torch.nn.functional.grid_sample(x1, torch.rand(1, 2, 2, 2))
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1, 2, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
grid_sampler(): expected grid to have size 3 in last dimension, but got grid with sizes [1, 2, 2, 2]

jit:
Failed running call_function <function grid_sample at 0x7f62b275a310>(*(FakeTensor(..., size=(1, 1, 2, 2, 2)), FakeTensor(..., size=(1, 2, 2, 2))), **{}):
grid_sampler(): expected grid to have size 3 in last dimension, but got grid with sizes torch.Size([1, 2, 2, 2])

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''