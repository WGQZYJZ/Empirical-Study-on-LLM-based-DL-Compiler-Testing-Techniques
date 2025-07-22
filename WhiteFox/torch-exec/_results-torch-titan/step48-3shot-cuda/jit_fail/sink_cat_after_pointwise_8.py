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
        x = x.view(1, x.shape[0], (- 1)).transpose(1, 2).view(x.shape[0], (- 1)).transpose(0, 1)
        return torch.pow(x, 2.0).tanh()




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 12, 2)), 2, -1), **{}):
Cannot view a tensor with shape torch.Size([1, 12, 2]) and strides (24, 1, 12) as a tensor with shape (2, 12)!

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''