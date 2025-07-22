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
        self.conv = torch.nn.Conv2d(3, 32, 5, padding=4, dilation=3)
        self.fc = torch.nn.Linear(448, 10)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 - 2.1)
        v3 = F.relu(v2)
        v4 = torch.flatten(v3, 1)
        v5 = self.fc(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1548800 and 448x10)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 1548800)),), **{}):
a and b must have same reduction dim, but got [1, 1548800] X [448, 10].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''