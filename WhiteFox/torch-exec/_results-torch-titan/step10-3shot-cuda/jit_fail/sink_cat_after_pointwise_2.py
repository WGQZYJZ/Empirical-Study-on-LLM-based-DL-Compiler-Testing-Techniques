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
        y = x.view(x.shape[0], (- 1))
        if True:
            k = y.view(x.shape[0], (- 1)).sin()
            if False:
                k = torch.cat([k, k], dim=1)
        if (k.shape[1] == 9):
            y = y.view(x.shape[0], (- 1), y.shape[1]).permute(1, 0, 2)
        z = torch.tanh(k)
        for i in range(0, 3):
            if (i == 1):
                if True:
                    z = z.reshape(2, 3, (- 1)).permute(1, 0, 2)
            else:
                z.view(2, (- 1))
        z = torch.tanh(z)
        return z




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(3, 2, 4)), 2, -1), **{}):
Cannot view a tensor with shape torch.Size([3, 2, 4]) and strides (4, 12, 1) as a tensor with shape (2, 12)!

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''