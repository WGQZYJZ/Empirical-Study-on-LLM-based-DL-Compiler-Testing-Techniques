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
        self.v1 = torch.randn(16, 2, 3, 3)

    def forward(self, x1):
        v2 = self.v1
        v3 = torch.nn.functional.conv2d(x1, v2, padding=1, stride=1)
        v4 = torch.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 2, 3, 3], expected input[1, 1, 64, 64] to have 2 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x78da9bc699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64)), FakeTensor(..., device='cuda:0', size=(16, 2, 3, 3))), **{'padding': 1, 'stride': 1}):
Given groups=1, weight of size [16, 2, 3, 3], expected input[1, 1, 64, 64] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''