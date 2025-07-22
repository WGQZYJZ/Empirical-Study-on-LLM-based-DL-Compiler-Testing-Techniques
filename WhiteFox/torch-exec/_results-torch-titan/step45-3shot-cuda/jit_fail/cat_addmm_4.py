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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(5, 5)
        self.cat = torch.cat
        self.stack = torch.stack

    def forward(self, x):
        x = self.layers(x)
        x = self.stack([x, x, x], dim=1)
        x = x.transpose(0, 1)
        x = x.view((- 1))
        x = self.cat([x, x, x], dim=1)
        x = self.stack([x, x, x], dim=1)
        (x, _) = torch.max(x, dim=0)
        return x




func = Model().to('cuda')



x = torch.randn(5, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(3, 5, 5)), -1), **{}):
Cannot view a tensor with shape torch.Size([3, 5, 5]) and strides (5, 15, 1) as a tensor with shape (75,)!

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''