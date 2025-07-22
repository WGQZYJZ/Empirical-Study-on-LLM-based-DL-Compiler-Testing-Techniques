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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(128, 3, 3, 1, 1), torch.nn.Conv2d(64, 32, 3, 1, 1), torch.nn.Conv2d(32, 128, 3, 1, 1), torch.nn.Conv2d(16, 64, 3, 1, 1))

    def forward(self, x1):
        v1 = self.features(x1)
        split_tensors = torch.split(v1, [1, 1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return concatenated_tensor




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 128, 3, 3], expected input[1, 16, 64, 64] to have 128 channels, but got 16 channels instead

jit:
Failed running call_module L__self___features_0(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)),), **{}):
Given groups=1, weight of size [3, 128, 3, 3], expected input[1, 16, 64, 64] to have 128 channels, but got 16 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''