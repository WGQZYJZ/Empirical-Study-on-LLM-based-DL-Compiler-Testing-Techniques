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
        super(Model, self).__init__()
        self.conv2d = torch.nn.Conv2d(100, 284, 16, stride=16)

    def forward(self, input1):
        t1 = self.conv2d(input1)
        return t1




func = Model().to('cuda')



input1 = torch.randn(1, 100, 7, 7)


test_inputs = [input1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (7 x 7). Kernel size: (16 x 16). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(1, 100, 7, 7)),), **{}):
Calculated padded input size per channel: (7 x 7). Kernel size: (16 x 16). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''