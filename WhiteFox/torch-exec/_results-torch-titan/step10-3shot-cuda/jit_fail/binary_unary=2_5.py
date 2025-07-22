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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=2, padding=1, dilation=2)
        self.softmax = torch.nn.Softmax2d()

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.relu(v1)
        v3 = torch.squeeze(v2, 0)
        v4 = v3.reshape(1, (- 1))
        v5 = self.softmax(v4)
        v6 = (v4 * v5)
        v7 = torch.reshape(v6, (1, 8, 30, 30))
        v8 = torch.squeeze(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Softmax2d: expected input to be 3D or 4D, got 2D instead

jit:
Failed running call_module L__self___softmax(*(FakeTensor(..., device='cuda:0', size=(1, 98568)),), **{}):
Softmax2d: expected input to be 3D or 4D, got 2D instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''