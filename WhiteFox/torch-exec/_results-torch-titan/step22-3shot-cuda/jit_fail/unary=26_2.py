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
        self.conv_t = torch.nn.ConvTranspose2d(428, 64, (47, 10), stride=1, padding=(46, 9), groups=1, bias=True)
        self.conv = torch.nn.Conv3d(16, 10, (3, 7, 3), stride=(1, 2, 2), padding=(1, 3, 1), dilation=(1, 1, 1), groups=1, bias=True)

    def forward(self, x):
        v1 = self.conv_t(x)
        v2 = self.conv(v1)
        return v2




func = Model().to('cuda')



x = torch.randn(8, 16, 428, 117, 39)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [8, 16, 428, 117, 39]

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(8, 16, 428, 117, 39)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [8, 16, 428, 117, 39]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''