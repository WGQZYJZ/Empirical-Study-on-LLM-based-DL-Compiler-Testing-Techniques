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

class Model(nn.Module):

    def __init__(self, negative_slope):
        super().__init__()
        self.linear = nn.Linear(3, 8)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float()
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


negative_slope = 1
func = Model(0.001).to('cpu')


x1 = torch.randn(1, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
where expected condition to be a boolean tensor, but got a tensor with dtype Float

jit:
Failed running call_function <built-in method where of type object at 0x799a6cb96ec0>(*(FakeTensor(..., size=(1, 8)), FakeTensor(..., size=(1, 8)), FakeTensor(..., size=(1, 8))), **{}):
expected predicate to be bool, got torch.float32

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''