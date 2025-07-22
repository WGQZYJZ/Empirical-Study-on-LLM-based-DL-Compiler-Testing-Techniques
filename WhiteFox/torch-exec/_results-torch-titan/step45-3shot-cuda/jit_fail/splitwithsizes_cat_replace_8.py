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
        block_0 = [torch.nn.Conv2d(3, 32, 3, 1, 1, bias=False)]
        block_1 = [torch.nn.ReLU()]
        block_2 = [torch.nn.Conv2d(32, 64, 3, 2, 1, bias=False), torch.nn.BatchNorm2d(64, affine=False, track_running_stats=False)]
        block_3 = [torch.nn.ReLU()]
        block_4 = [torch.nn.Conv2d(32, 64, 1, 1, 1, bias=False)]
        self.features = torch.nn.Sequential(*block_0, *block_1, *block_2, *block_3, *block_4)

    def forward(self, v1):
        x = self.features(v1)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 32, 1, 1], expected input[1, 64, 32, 32] to have 32 channels, but got 64 channels instead

jit:
Failed running call_module L__self___features_5(*(FakeTensor(..., device='cuda:0', size=(1, 64, 32, 32)),), **{}):
Given groups=1, weight of size [64, 32, 1, 1], expected input[1, 64, 32, 32] to have 32 channels, but got 64 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''