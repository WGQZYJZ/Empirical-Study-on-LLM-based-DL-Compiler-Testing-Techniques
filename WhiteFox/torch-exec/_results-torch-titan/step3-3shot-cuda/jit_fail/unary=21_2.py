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
        self.conv = torch.nn.Conv2d((3 + (4 * 5)), 8, 1, stride=1, padding=1)

    def forward(self, input):
        x = self.conv(input)
        return x




func = ModelTanh().to('cuda')



input = torch.randn(1, 3, 64, 64)


test_inputs = [input]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 23, 1, 1], expected input[1, 3, 64, 64] to have 23 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [8, 23, 1, 1], expected input[1, 3, 64, 64] to have 23 channels, but got 3 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''