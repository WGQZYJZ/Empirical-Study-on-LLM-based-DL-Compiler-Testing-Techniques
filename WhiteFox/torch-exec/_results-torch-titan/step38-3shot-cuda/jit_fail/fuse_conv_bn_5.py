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
        self.conv1 = torch.nn.Conv2d(7, 7, 3)
        self.relu1 = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(7, 7, 1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.conv2(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 3, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [7, 7, 3, 3], expected input[1, 3, 4, 4] to have 7 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 4, 4)),), **{}):
Given groups=1, weight of size [7, 7, 3, 3], expected input[1, 3, 4, 4] to have 7 channels, but got 3 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''