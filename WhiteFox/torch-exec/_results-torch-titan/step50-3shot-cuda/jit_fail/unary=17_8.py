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
        self.block0 = torch.nn.Sequential(torch.nn.ConvTranspose3d(1, 1, 4, padding=1, stride=1), torch.nn.ReLU(inplace=False))
        self.block1 = torch.nn.Sequential(torch.nn.Conv2d(1, 1, 1, padding=1, stride=1), torch.nn.ReLU(inplace=False))

    def forward(self, x1):
        y1 = self.block0(x1)
        y2 = self.block1(y1)
        return y2




func = Model().to('cuda')



x1 = torch.randn(1, 1, 32, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 1, 33, 33, 33]

jit:
Failed running call_module L__self___block1_0(*(FakeTensor(..., device='cuda:0', size=(1, 1, 33, 33, 33)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 1, 33, 33, 33]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''