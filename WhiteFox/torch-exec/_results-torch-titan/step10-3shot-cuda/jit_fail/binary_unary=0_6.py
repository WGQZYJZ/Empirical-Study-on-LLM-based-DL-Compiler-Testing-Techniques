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
        self.conv = torch.nn.Conv2d(3, 16, 3, stride=2, padding=1)
        self.fc = torch.nn.Linear(in_features=12288, out_features=10)

    def forward(self, x):
        v0 = torch.flatten(x, 1)
        v1 = self.conv(x)
        v2 = v1.mean([2, 3])
        v3 = torch.cat((v0, v2), 1)
        v4 = self.fc(v3)
        v5 = torch.softmax(v4, dim=1)
        return v5




func = Model().to('cuda')



x = torch.randn(1, 3, 224, 224)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x150544 and 12288x10)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 150544)),), **{}):
a and b must have same reduction dim, but got [1, 150544] X [12288, 10].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''