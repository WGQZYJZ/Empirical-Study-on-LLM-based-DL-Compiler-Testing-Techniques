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
        self.layers = nn.Linear(3, 4)

    def forward(self, x):
        x = self.layers(x)
        x = torch.zeros_like(x).repeat(3, 4).to(x.device)
        x = x.permute(1, 0).view(4, (- 1)).transpose(1, 0)
        x = x.permute(1, 0)
        return x




func = Model().to('cuda')



x = torch.randn(2, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(16, 6)), 4, -1), **{}):
Cannot view a tensor with shape torch.Size([16, 6]) and strides (1, 16) as a tensor with shape (4, 24)!

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''