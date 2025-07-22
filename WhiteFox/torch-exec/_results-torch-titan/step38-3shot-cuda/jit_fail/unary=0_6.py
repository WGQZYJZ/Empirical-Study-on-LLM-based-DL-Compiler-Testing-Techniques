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
        self.conv1 = torch.nn.Conv3d(1, 2, kernel_size=[16, 3, 99], stride=[4, 1, 2])
        self.conv2 = torch.nn.Conv2d(2, 4, kernel_size=3, stride=2)

    def forward(self, x2):
        v3 = self.conv1(x2)
        v4 = self.conv2(v3)
        v5 = (v4 * 0.5)
        v7 = (v5 * 0.707106)
        v6 = (v5 * float('1e-22'))
        v8 = (v6 * 0.507106)
        v9 = (v8 * 0.707106)
        v10 = (v9 * 0.707106)
        return v10




func = Model().to('cuda')



x2 = torch.randn(1, 1, 24, 487, 799)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 2, 3, 485, 351]

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 485, 351)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 2, 3, 485, 351]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''