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
        self.conv0 = torch.nn.Conv2d(2, 2, 1).cuda()
        self.linear = torch.nn.Linear(6, 2)

    def forward(self, x1):
        v4 = x1
        v1 = self.conv0(v4)
        v2 = v1.permute(0, 3, 1, 2)
        v3 = v2.view(v2.size(0), (- 1))
        v5 = v3.cuda()
        v = torch.nn.functional.linear(v5, self.linear.weight, self.linear.bias)
        return v




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, 2, device='cuda')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)), 1, -1), **{}):
Cannot view a tensor with shape torch.Size([1, 2, 2, 2]) and strides (8, 1, 4, 2) as a tensor with shape (1, 8)!

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''