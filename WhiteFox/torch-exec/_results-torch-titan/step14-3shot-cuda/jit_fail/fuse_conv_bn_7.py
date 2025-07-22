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
        self.conv1 = torch.nn.Conv2d(1, 1, 4)
        self.conv2 = torch.nn.Conv2d(1, 1, 2)
        self.conv3 = torch.nn.Conv2d(1, 1, 1)

    def forward(self, x):
        t1 = self.conv1(x)
        t2 = (self.conv2(t1) if (t1 is not None) else None)
        t7 = (self.conv3(t2) if (t2 is not None) else None)
        return t7




func = Model().to('cuda')



x = torch.randn(1, 3, 3, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 4, 4], expected input[1, 3, 3, 3] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 3, 3)),), **{}):
Given groups=1, weight of size [1, 1, 4, 4], expected input[1, 3, 3, 3] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''