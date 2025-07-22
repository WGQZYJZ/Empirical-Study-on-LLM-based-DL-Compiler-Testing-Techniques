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

    def forward(self, x):
        y = x.permute((0, 2, 3, 1))
        y = y.view(y.shape[0], -1)
        return y



func = Model().to('cpu')


x = torch.randn(2, 2, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.

jit:
Failed running call_method view(*(FakeTensor(..., size=(s0, s2, s3, s1)), s0, -1), **{}):
Cannot view a tensor with shape torch.Size([s0, s2, s3, s1]) and strides (s1*s2*s3, s3, 1, s2*s3) as a tensor with shape (s0, s1*s2*s3)!

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''