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



class Example(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = torch.nn.Sequential(torch.nn.Conv2d(3, 10, 5), torch.nn.BatchNorm2d(10), torch.nn.MaxPool2d(2), torch.nn.ReLU(), torch.nn.Conv2d(10, 2, 5))

    def forward(self, x):
        x = self.layers(x)
        return x




func = Example().to('cuda')



x = torch.randn(1, 3, 10, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (3 x 3). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___layers_4(*(FakeTensor(..., device='cuda:0', size=(1, 10, 3, 3)),), **{}):
Calculated padded input size per channel: (3 x 3). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''