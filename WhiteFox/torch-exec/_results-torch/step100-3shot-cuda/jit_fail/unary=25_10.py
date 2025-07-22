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

    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0.0
        v3 = v2 * self.negative_slope
        v4 = torch.where(v1, v1, v3)
        return v4


func = Model().to('cuda')


x1 = torch.randn(2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
where expected condition to be a boolean tensor, but got a tensor with dtype Float

jit:
Failed running call_function <built-in method where of type object at 0x709b4a396ec0>(*(FakeTensor(..., device='cuda:0', size=(2, 4)), FakeTensor(..., device='cuda:0', size=(2, 4)), FakeTensor(..., device='cuda:0', size=(2, 4))), **{}):
expected predicate to be bool, got torch.float32

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''