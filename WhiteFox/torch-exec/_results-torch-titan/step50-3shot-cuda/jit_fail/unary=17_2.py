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
        self.block0 = torch.nn.Sequential(torch.nn.ConvTranspose3d(2, 5, 3, padding=1, stride=1), torch.nn.ReLU(inplace=True))
        self.conv0 = torch.nn.ConvTranspose2d(6, 1, 3, padding=1, stride=1)

    def forward(self, x1):
        z = self.block0(x1)
        y = self.conv0(z)
        return y




func = Model().to('cuda')



x1 = torch.randn(2, 2, 8, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [2, 5, 8, 8, 8]

jit:
Failed running call_module L__self___conv0(*(FakeTensor(..., device='cuda:0', size=(2, 5, 8, 8, 8)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [2, 5, 8, 8, 8]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''