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
        self.features = torch.nn.Sequential(torch.nn.MaxPool2d(3, 2, 1, 1), torch.nn.MaxPool2d(5, 4, 2, 2), torch.nn.MaxPool2d(3, 1, 1, 0))
        self.convolution = torch.nn.Conv2d(3, 3, 3, 1, 1)

    def forward(self, x1):
        v1 = self.features(x1)
        v1 = self.convolution(v1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
dilation should be greater than zero, but got dilationH: 0 dilationW: 0

jit:
Failed running call_module L__self___features_2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 7, 7)),), **{}):
dilation should be greater than zero, but got dilationH: {dilationH}, dilationW: {dilationW}

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''