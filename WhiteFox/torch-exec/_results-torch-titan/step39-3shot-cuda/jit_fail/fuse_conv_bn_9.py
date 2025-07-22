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
        super(Model, self).__init__()
        self.conv = torch.nn.Conv2d(2, 2, kernel_size=(4, 4), stride=(4, 4))
        self.bn0 = torch.nn.BatchNorm2d(2)
        self.bn1 = torch.nn.BatchNorm2d(2)
        self.bn = torch.nn.BatchNorm2d(2)
        self.output = torch.nn.Linear(2, 2)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn0(x)
        x = self.bn1(x)
        x = self.bn(x)
        return self.output(x)




func = Model().to('cuda')



x = torch.randn(1, 2, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x1 and 2x2)

jit:
Failed running call_module L__self___output(*(FakeTensor(..., device='cuda:0', size=(1, 2, 1, 1)),), **{}):
a and b must have same reduction dim, but got [2, 1] X [2, 2].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''