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
        self.conv1 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.ln1 = torch.nn.LayerNorm((16, 16, 16), elementwise_affine=True)
        self.bn1 = torch.nn.BatchNorm3d(16)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(x2)
        v4 = self.ln1(((v1 + v2) + v3))
        v5 = self.bn1(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16, 16)



x2 = torch.randn(1, 3, 16, 16, 16)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 3, 16, 16, 16]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 16, 16, 16)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 3, 16, 16, 16]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''