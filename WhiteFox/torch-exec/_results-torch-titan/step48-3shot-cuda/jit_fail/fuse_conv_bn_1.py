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
        self.bn = torch.nn.BatchNorm2d(3, affine=True, momentum=0.5)
        self.conv = torch.nn.Conv2d(3, 3, 3)
        self.bias = torch.nn.Parameter(torch.empty(3))

    def forward(self, x2):
        x2 = self.conv(x2)
        x2 = self.bn(x2)
        bias = self.bias.expand_as(x)
        return (x2 + bias)




func = Model().to('cuda')



x2 = torch.randn(1, 3, 4, 4)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
name 'x' is not defined

jit:
name 'x' is not defined

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''