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
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bmm1 = torch.nn.Bilinear(8, 8, 8)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.bn1(v1)
        v3 = v2.softmax(dim=1)
        v4 = x2.bmm(v3).relu()
        v5 = self.bmm1(v1, v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(16, 3, 32, 32)



x2 = torch.randn(8, 3, 16, 16)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
batch1 must be a 3D tensor

jit:
Failed running call_method bmm(*(FakeTensor(..., device='cuda:0', size=(8, 3, 16, 16)), FakeTensor(..., device='cuda:0', size=(16, 8, 34, 34))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''