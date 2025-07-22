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
        self.conv = torch.nn.Conv2d(3, 48, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(((48 * 14) * 15), 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v1 = v1.view(v1.size(0), (- 1))
        v1 = self.fc(v1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x209088 and 10080x1)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 209088)),), **{}):
a and b must have same reduction dim, but got [1, 209088] X [10080, 1].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''