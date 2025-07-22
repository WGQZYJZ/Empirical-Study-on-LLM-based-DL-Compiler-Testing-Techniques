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
        self.conv = torch.nn.Conv3d(4, 4, 3)
        self.norm = torch.nn.BatchNorm3d(4)

    def forward(self, x2):
        x = self.conv(x2)
        x = self.norm(x)
        x = self.conv(x)
        return x




func = Model().to('cuda')



x2 = torch.randn(1, 4, 4, 3, 3)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 1 x 1). Kernel size: (3 x 3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 4, 2, 1, 1)),), **{}):
Calculated padded input size per channel: (2 x 1 x 1). Kernel size: (3 x 3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''