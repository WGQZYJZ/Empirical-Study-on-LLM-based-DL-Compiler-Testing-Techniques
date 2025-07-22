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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=0)
        self.linear = torch.nn.Linear(((8 * 56) * 56), 10)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v2 = v2.reshape(v2.size()[0], (- 1))
        v3 = self.linear(v2)
        v4 = F.log_softmax(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x394272 and 25088x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 394272)),), **{}):
a and b must have same reduction dim, but got [1, 394272] X [25088, 10].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''