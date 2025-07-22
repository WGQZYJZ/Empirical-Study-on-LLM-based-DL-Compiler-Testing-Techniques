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
        self.conv = torch.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.fc = torch.nn.Linear(in_features=1024, out_features=10)

    def forward(self, x1):
        v1 = self.conv(x1)
        v1_resized = (((v1[:, :, 1:, 1:] + v1[:, :, :(- 1), 1:]) + v1[:, :, 1:, :(- 1)]) + v1[:, :, :(- 1), :(- 1)]).unsqueeze(1)
        v2 = v1_resized.view([v1_resized.shape[0], (- 1)])
        v3 = self.fc(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 32, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x30752 and 1024x10)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 30752)),), **{}):
a and b must have same reduction dim, but got [1, 30752] X [1024, 10].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''