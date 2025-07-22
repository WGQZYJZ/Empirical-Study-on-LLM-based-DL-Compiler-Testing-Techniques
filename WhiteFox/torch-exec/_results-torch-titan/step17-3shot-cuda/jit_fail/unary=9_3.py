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

    def forward(self, x1):
        v1 = torch.conv2d(x1, torch.ones(8, 3, 1, 1), padding=1, groups=8, bias=None)
        v2 = (v1 + 3)
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = torch.div(v3, 6)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=8, weight of size [8, 3, 1, 1], expected input[1, 3, 64, 64] to have 24 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7439780699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., size=(8, 3, 1, 1))), **{'padding': 1, 'groups': 8, 'bias': None}):
Given groups=8, weight of size [8, 3, 1, 1], expected input[1, 3, 64, 64] to have 24 channels, but got 3 channels instead

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''