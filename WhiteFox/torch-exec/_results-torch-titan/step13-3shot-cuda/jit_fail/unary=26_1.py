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
        self.conv_t = torch.nn.ConvTranspose1d(1, 2, (2,), stride=2, padding=1, bias=False)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        x2 = self.conv_t(x)
        x3 = self.relu(x2)
        x4 = (x2 > 0)
        x5 = (x2 * x3)
        x6 = torch.where(x4, x2, x5)
        return x6




func = Model().to('cuda')



x = torch.randn(1, 1, 5, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 1, 5, 1]

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., size=(1, 1, 5, 1)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 1, 5, 1]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''