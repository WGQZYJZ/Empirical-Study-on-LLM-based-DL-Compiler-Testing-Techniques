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
        self.conv1 = torch.nn.Conv2d(3, 8, 5, stride=2, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = x2 - v1
        v3 = F.relu(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (15) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(1, 3, 64, 64)), FakeTensor(..., size=(1, 8, (((s1 - 3)//2)) + 1, (((s2 - 3)//2)) + 1))), **{}):
The size of tensor a (64) must match the size of tensor b ((((s2 - 3)//2)) + 1) at non-singleton dimension 3)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''