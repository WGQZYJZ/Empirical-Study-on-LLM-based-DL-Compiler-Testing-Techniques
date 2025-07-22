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
        self.conv1 = torch.nn.Sequential(torch.nn.Conv2d(3, 64, (1, 3), stride=1, padding=0), torch.nn.BatchNorm2d(64), torch.nn.Flatten(), torch.nn.Linear(65536, 13))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3182592 and 65536x13)

jit:
Failed running call_module L__self___conv1_3(*(FakeTensor(..., device='cuda:0', size=(1, 3182592)),), **{}):
a and b must have same reduction dim, but got [1, 3182592] X [65536, 13].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''