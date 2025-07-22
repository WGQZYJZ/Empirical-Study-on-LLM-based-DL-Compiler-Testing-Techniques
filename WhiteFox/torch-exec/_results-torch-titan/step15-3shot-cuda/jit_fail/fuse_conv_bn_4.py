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



class M(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1, x2):
        y1 = self.conv(x1)
        y2 = self.conv(x2)
        y = self.bn(y1)
        out = torch.cat((4 * [y]), 1)
        return torch.add(y2, out)




func = M().to('cuda')



x1 = torch.randn(1, 3, 4, 4)



x2 = torch.randn(1, 3, 1, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 1, 1)),), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''