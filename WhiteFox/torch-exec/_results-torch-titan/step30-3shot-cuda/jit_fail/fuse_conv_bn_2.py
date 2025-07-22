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
        m = torch.nn.MaxPool2d(2)
        c = torch.nn.Conv2d(3, 3, 3)
        self.layer = torch.nn.Sequential(m, c)

    def forward(self, x):
        c = self.layer(x)
        return (c, x)




func = Model().to('cuda')



x = torch.randn(2, 3, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___layer_1(*(FakeTensor(..., device='cuda:0', size=(2, 3, 2, 2)),), **{}):
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''