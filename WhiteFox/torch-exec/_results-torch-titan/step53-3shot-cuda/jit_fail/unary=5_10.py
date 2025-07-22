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
        self.conv_transpose = torch.nn.ConvTranspose2d(12, 100, 3, padding=1)
        self.conv2d = torch.nn.Conv2d(11, 52, 3, padding=1)

    def forward(self, x1, h1):
        v1 = self.conv_transpose(x1)
        h1 = h1.expand(v1.shape[0], (- 1), v1.shape[(- 2)], v1.shape[(- 1)])
        v2 = torch.cat([v1, h1], 1)
        v3 = self.conv2d(v2)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v1 * v5)
        return (v6, v5)




func = Model().to('cuda')



x1 = torch.randn(1, 12, 65, 65)



h1 = torch.randn(1, 100, 2, 2)


test_inputs = [x1, h1]

# JIT_FAIL
'''
direct:
The expanded size of the tensor (65) must match the existing size (2) at non-singleton dimension 3.  Target sizes: [1, -1, 65, 65].  Tensor sizes: [1, 100, 2, 2]

jit:
Failed running call_method expand(*(FakeTensor(..., device='cuda:0', size=(1, 100, 2, 2)), 1, -1, 65, 65), **{}):
expand: attempting to expand a dimension of length 2!

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''