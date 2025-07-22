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
        self.conv = torch.nn.Conv2d(8, 8, 7, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * torch.tensor([3.57680109, 0.20652153, 0.0, 0.0, 0.13794327, 0.0, 0.08564419, 0.01622201])
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 8, 20, 20)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (14) must match the size of tensor b (8) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 8, s1 - 6, s2 - 6)), FakeTensor(..., size=(8,))), **{}):
The size of tensor a (s2 - 6) must match the size of tensor b (8) at non-singleton dimension 3)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''