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
        self.conv1 = torch.nn.Conv1d(4, 32, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1 = torch.nn.BatchNorm3d(32)
        self.conv2 = torch.nn.Conv3d(32, 32, kernel_size=1, stride=(1, 1, 1), padding=0, bias=False)
        self.bn2 = torch.nn.BatchNorm2d(32)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x4):
        v1 = x4.to(torch.float16)
        v2 = self.conv1(v1)
        v3 = self.bn1(v2)
        v4 = v3.to(torch.float32)
        v5 = self.conv2(v4)
        v6 = self.bn2(v5)
        return self.sigmoid(v6)




func = Model().to('cuda')



x4 = torch.randn(1, 4, 160, 5)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 4, 160, 5]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 4, 160, 5), dtype=torch.float16),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 4, 160, 5]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''