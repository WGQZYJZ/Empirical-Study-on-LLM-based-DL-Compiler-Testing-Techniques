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
        self.conv_branch = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(8)

    def forward(self, x1):
        v1 = self.conv(x1)
        v1 = (v1 + 1)
        v1 = F.sigmoid(v1)
        v1 = self.bn(v1)
        v1 = torch.add(v1, 1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 8, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv'

jit:
conv

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''