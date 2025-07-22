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
        self.conv = torch.nn.Conv2d(3, 4, 2)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = self.conv(x)
        x = torch.flatten(x, 1)
        x = self.bn(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 3, 16, 16)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 768]

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 768)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 768]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''