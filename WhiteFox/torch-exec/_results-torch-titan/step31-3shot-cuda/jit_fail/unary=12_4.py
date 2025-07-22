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
        self.relu = torch.nn.ReLU()
        self.conv = torch.nn.Conv2d(3, 8, 7, stride=1, padding=3)

    def forward(self, x1):
        v1 = self.relu(x1)
        v2 = self.conv(v1)
        v3 = v2.sum(dim=(- 1)).sum(dim=(- 1)).expand_as(v1)
        v4 = self.relu(v1)
        v5 = self.conv(v4)
        v6 = (v5 * v3)
        v7 = v6.sum(dim=(- 1)).sum(dim=(- 1)).expand_as(v1)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The expanded size of the tensor (64) must match the existing size (8) at non-singleton dimension 3.  Target sizes: [1, 3, 64, 64].  Tensor sizes: [1, 8]

jit:
Failed running call_method expand_as(*(FakeTensor(..., device='cuda:0', size=(1, 8)), FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64))), **{}):
expand: attempting to expand a dimension of length 8!

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''