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
        self.conv1 = torch.nn.Conv1d(4, 6, 2)
        self.conv2 = torch.nn.Conv2d(1, 1, 1)
        self.conv3 = torch.nn.Conv2d(1, 1, 1)
        self.conv4 = torch.nn.Conv2d(3, 5, 7, stride=(2, 1), padding=(2, 3), dilation=(1, 1))

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(x)
        v3 = self.conv3(v1)
        v4 = self.conv4(v2)
        v5 = torch.tanh(v4)
        return v5




func = ModelTanh().to('cuda')



x = torch.randn(35, 4, 26)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 35, 4, 26] to have 1 channels, but got 35 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(35, 4, 26)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 35, 4, 26] to have 1 channels, but got 35 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''