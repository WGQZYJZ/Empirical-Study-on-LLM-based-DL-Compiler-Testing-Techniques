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
        self.conv = torch.nn.Conv2d(3, 3, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - torch.randn(1, 3, 3, 3)
        return v2



func = Model().to('cuda')


x = torch.randn(1, 3, 5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (3) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 3, s1, s2)), FakeTensor(..., size=(1, 3, 3, 3))), **{}):
The size of tensor a (s2) must match the size of tensor b (3) at non-singleton dimension 3)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''