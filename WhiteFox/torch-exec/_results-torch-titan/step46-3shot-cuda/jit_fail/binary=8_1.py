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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bn2 = torch.nn.BatchNorm2d(8)

    def forward(self, x1, x2, extra):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = (v1 + v2)
        v4 = self.bn1(v3, eps=extra)
        v5 = self.bn2(v3, eps=extra)
        v6 = (v4 * v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)



extra = torch.randn(1, 8, 1, 1)


test_inputs = [x1, x2, extra]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'eps'

jit:
Failed running call_module L__self___bn1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)),), **{'eps': FakeTensor(..., device='cuda:0', size=(1, 8, 1, 1))}):
forward() got an unexpected keyword argument 'eps'

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''