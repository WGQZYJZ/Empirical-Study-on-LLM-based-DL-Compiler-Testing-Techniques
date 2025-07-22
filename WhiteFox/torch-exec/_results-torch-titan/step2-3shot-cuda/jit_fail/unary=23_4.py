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
        self.conv_transpose1 = torch.nn.ConvTranspose3d(6, 9, 1, stride=1, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(9, 3, 1, stride=1, padding=1)

    def forward(self, x1):
        t1 = self.conv_transpose1(x1)
        t2 = torch.atan(t1)
        t3 = self.conv_transpose2(t2)
        v1 = torch.atan(t3)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 6, 32, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 9, 30, 62, 62]

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(1, 9, 30, 62, 62)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 9, 30, 62, 62]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''