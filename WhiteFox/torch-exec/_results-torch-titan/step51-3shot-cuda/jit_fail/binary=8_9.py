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
        self.conv1 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = torch.flatten(v1)
        v4 = torch.flatten(v2)
        v5 = (v3 + v4)
        v6 = self.conv3(v5)
        v7 = self.conv4(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 8, 256, 256)



x2 = torch.randn(1, 8, 256, 256)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1048576]

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1048576,)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1048576]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''