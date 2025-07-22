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
        self.conv = torch.nn.Conv2d(20, 8, 1, stride=1, padding=0)

    def forward(self, x1, other):
        v1 = self.conv(x1)
        v2 = (v1 + other)
        v3 = torch.cat([v2, other, other])
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 20, 64, 64)

other = 1

test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
expected Tensor as element 1 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x73051b6699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)), 1, 1],), **{}):
expected Tensor as element 1 in argument 0, but got int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''