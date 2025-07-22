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
        self.conv1 = torch.nn.Conv3d(4, 4, 4)
        self.bn = torch.nn.BatchNorm3d(4)
        self.conv2 = torch.nn.Conv3d(1, 1, 1)
        self.bn1 = torch.nn.BatchNorm3d(4)
        self.relu = torch.nn.ReLU(inplace=True)

    def forward(self, x1):
        x1 = self.conv1(x1)
        x1 = self.relu(self.bn1(x1))
        x1 = torch.transpose(x1, 1, 2)
        x1 = torch.bmm(x1.unsqueeze(1), x1.unsqueeze(2))
        x1 = torch.cat([x1.flatten(1), x1.flatten(0)], (- 1))
        x2 = self.conv2(x1)
        x1 = self.bn(x2)
        return (x1, x2)




func = Model().to('cuda')



x1 = torch.randn(1, 4, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 4, 4, 4, 4], expected input[1, 1, 4, 8, 8] to have 4 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 4, 8, 8)),), **{}):
Given groups=1, weight of size [4, 4, 4, 4, 4], expected input[1, 1, 4, 8, 8] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''