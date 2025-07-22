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
        self.conv1 = torch.nn.Conv2d(16, 32, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(32, 64, 7, stride=1, padding=3)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = torch.cat([v2, x2], dim=1)
        v4 = self.conv2(v3)
        v5 = (v4 * x2)
        v6 = torch.nn.functional.avg_pool2d(v5, 2, stride=1)
        (_, max_idx) = torch.max(v6.view(1, (- 1)), 1)
        max_y = ((max_idx // 8) * 2)
        max_x = ((max_idx % 8) * 2)
        return v5[:, :, max_y:(max_y + 7), max_x:(max_x + 7)]




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 32, 7, 7], expected input[1, 48, 64, 64] to have 32 channels, but got 48 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 48, 64, 64)),), **{}):
Given groups=1, weight of size [64, 32, 7, 7], expected input[1, 48, 64, 64] to have 32 channels, but got 48 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''