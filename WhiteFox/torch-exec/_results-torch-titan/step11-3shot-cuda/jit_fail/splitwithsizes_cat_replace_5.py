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



class Split_with_Sizes_Concat(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.features = torch.nn.Sequential(torch.nn.Conv2d(1, 1, 3, 1, 0), torch.nn.ReLU(), torch.nn.MaxPool2d(3, 2, 0))

    def forward(self, x1):
        v1 = self.features(x1)
        return (v1,)




func = Split_with_Sizes_Concat().to('cuda')



x1 = torch.randn(1, 3, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 3, 16, 16] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___features_0(*(FakeTensor(..., device='cuda:0', size=(1, 3, 16, 16)),), **{}):
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 3, 16, 16] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''