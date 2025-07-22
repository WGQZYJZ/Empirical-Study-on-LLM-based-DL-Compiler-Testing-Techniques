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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(128, 2, kernel_size=1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(1, 8, 2, stride=(0, 1), padding=0)
        self.conv3 = torch.nn.Conv2d(8, 3, 2, stride=(0, 1), padding=1)

    def forward(self, x):
        v1 = self.conv1(x).reshape(1, (- 1))
        v2 = torch.tanh(v1)
        return self.conv3(self.conv2(v2).reshape((8 * 4), 120, 1, 2)).reshape(8, 4, 120, 2)




func = ModelTanh().to('cuda')



x = torch.randn(1, 2, 128, 25)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 128, 1, 1], expected input[1, 2, 128, 25] to have 128 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 2, 128, 25)),), **{}):
Given groups=1, weight of size [2, 128, 1, 1], expected input[1, 2, 128, 25] to have 128 channels, but got 2 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''