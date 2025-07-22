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
        self.conv1 = torch.nn.Conv2d(3, 3, 3)

    def forward(self, x):
        y = self.conv1(x)
        return (x, y)




func = Model().to('cuda')



x = torch.randn(1, 3, 1, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 1, 2)),), **{}):
Calculated padded input size per channel: (1 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''