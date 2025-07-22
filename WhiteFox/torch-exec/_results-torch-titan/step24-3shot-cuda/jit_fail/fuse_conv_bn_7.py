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
        self.conv = torch.nn.Conv3d(1, 1, 3, 1, 1)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 1, 6, 6, 6)


test_inputs = [x]

# JIT_FAIL
'''
direct:
expected 4D input (got 5D input)

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 1, 6, 6, 6)),), **{}):
expected 4D input (got 5D input)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''