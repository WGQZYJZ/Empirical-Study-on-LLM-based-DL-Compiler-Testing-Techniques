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
        torch.manual_seed(1)
        self.conv = torch.nn.Conv3d(2, 5, 5)
        torch.manual_seed(1)
        self.bn = torch.nn.BatchNorm3d(5)

    def forward(self, x2):
        y2 = self.conv(x2)
        y2 = self.bn(y2)
        return (y2 + y2)




func = Model().to('cuda')



x2 = torch.randn(1, 2, 2, 2, 2)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2 x 2). Kernel size: (5 x 5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2, 2)),), **{}):
Calculated padded input size per channel: (2 x 2 x 2). Kernel size: (5 x 5 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''