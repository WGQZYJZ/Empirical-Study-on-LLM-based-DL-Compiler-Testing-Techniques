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
        return F.conv1d(x1, torch.randn(10, 3, 2))



func = Model().to('cpu')


x1 = torch.randn(3, 1, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [10, 3, 2], expected input[3, 1, 10] to have 3 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv1d of type object at 0x733ea4f96ec0>(*(FakeTensor(..., size=(s0, 1, s1)), FakeTensor(..., size=(10, 3, 2))), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''