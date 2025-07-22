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
        self.layer1 = torch.nn.Conv2d(5, 4, 3)
        self.layer2 = torch.nn.BatchNorm2d(4)

    def forward(self, x1):
        x2 = self.layer1(x1)
        x3 = self.layer2(x2)
        del x3
        x4 = self.layer2(x1)
        return (x2, x4)




func = Model().to('cuda')



x1 = torch.randn(1, 5, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___layer1(*(FakeTensor(..., device='cuda:0', size=(1, 5, 2, 2)),), **{}):
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''