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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 5, 3, padding=1)

    def forward(self, x):
        t1 = self.conv(x)
        t2 = self.conv(t1)
        t3 = self.conv(t2)
        t4 = torch.tanh(t3)
        return




func = ModelTanh().to('cuda')



x = torch.randn(2, 1, 512, 512)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 1, 3, 3], expected input[2, 5, 512, 512] to have 1 channels, but got 5 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(2, 5, 512, 512)),), **{}):
Given groups=1, weight of size [5, 1, 3, 3], expected input[2, 5, 512, 512] to have 1 channels, but got 5 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''