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
        c = torch.nn.Conv2d(3, 32, kernel_size=1, padding=0)
        torch.manual_seed(5)
        c.weight = torch.nn.Parameter(torch.ones(c.weight.size()), requires_grad=False)
        self.conv1 = c
        self.relu1 = torch.nn.ReLU()
        self.conv2 = c
        self.relu2 = torch.nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.conv2(x)
        return self.relu2(x)




func = Model().to('cuda')



x = torch.randn(4, 3, 3, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 3, 1, 1], expected input[4, 32, 3, 3] to have 3 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(4, 32, 3, 3)),), **{}):
Given groups=1, weight of size [32, 3, 1, 1], expected input[4, 32, 3, 3] to have 3 channels, but got 32 channels instead

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''