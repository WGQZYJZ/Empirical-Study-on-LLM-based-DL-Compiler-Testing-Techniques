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
        self.conv1 = torch.nn.Conv2d(3, 7, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(7, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 2, 1, stride=1, padding=1)

    def forward(self, x1, other=1.7, padding1=None):
        var1 = self.conv1(x1)
        if (not (None in (padding1, padding2))):
            var1 += padding1
            var1 -= padding2
        var2 = self.conv2(var1)
        if (not (None in (padding1, padding2))):
            var2 += padding1
        var3 = self.conv3(var2)
        v2 = (var3 - other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'padding2' is not defined

jit:
name 'padding2' is not defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''