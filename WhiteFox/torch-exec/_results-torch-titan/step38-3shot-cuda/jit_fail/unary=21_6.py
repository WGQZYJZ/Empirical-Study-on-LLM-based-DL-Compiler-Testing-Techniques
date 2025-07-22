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
        self.conv1 = torch.nn.Conv2d(3, 11, 1)
        self.conv2 = torch.nn.Conv2d(3, 19, 1, padding=1)

    def forward(self, x):
        t1 = self.conv1(x)
        t2 = torch.tanh(t1)
        t3 = self.conv2(t2)
        t4 = torch.tanh(t3)
        return t4




func = ModelTanh().to('cuda')



x = torch.randn(1, 3, 28, 28)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [19, 3, 1, 1], expected input[1, 11, 28, 28] to have 3 channels, but got 11 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 11, 28, 28)),), **{}):
Given groups=1, weight of size [19, 3, 1, 1], expected input[1, 11, 28, 28] to have 3 channels, but got 11 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''