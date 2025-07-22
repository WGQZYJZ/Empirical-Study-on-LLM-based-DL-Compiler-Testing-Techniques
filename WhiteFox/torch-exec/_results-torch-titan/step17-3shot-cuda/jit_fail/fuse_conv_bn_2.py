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



class Module1(torch.nn.Module):

    def __init__(self):
        super(Module1, self).__init__()
        self.conv2d = torch.nn.Conv2d(3, 8, (3, 3), stride=(1, 1), padding=(1, 1), dilation=(1, 1), groups=1, bias=False)
        self.batchnorm2d = torch.nn.BatchNorm2d(8)

    def forward(self, x1):
        y1 = self.conv2d(x1)
        y2 = self.batchnorm2d(y1)
        return y2




func = Module1().to('cuda')



x1 = torch.randn(1, 6, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 6, 4, 4] to have 3 channels, but got 6 channels instead

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(1, 6, 4, 4)),), **{}):
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 6, 4, 4] to have 3 channels, but got 6 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''