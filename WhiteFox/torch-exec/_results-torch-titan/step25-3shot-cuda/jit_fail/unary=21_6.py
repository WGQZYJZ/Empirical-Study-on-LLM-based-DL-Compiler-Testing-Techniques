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
        self.conv1 = torch.nn.Conv2d(1, 1, 15, stride=2)
        self.conv2 = torch.nn.Conv2d(1, 1, 8, stride=3, padding=15)

    def forward(self, x):
        x = self.conv2(self.conv1(x))
        x = torch.tanh(x)
        return x




func = ModelTanh().to('cuda')



x = torch.randn(5, 5, 5, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 15, 15], expected input[5, 5, 5, 5] to have 1 channels, but got 5 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(5, 5, 5, 5)),), **{}):
Given groups=1, weight of size [1, 1, 15, 15], expected input[5, 5, 5, 5] to have 1 channels, but got 5 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''