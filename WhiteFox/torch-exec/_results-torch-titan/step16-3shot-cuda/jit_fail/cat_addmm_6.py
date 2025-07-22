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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(1, 1, 1, bias=False)

    def forward(self, x):
        x = self.conv(x)
        x = torch.cat((x, x), dim=1)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[2, 2, 2, 2] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(2, 2, 2, 2)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[2, 2, 2, 2] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''