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
        self.conv_t = torch.nn.ConvTranspose2d(242, 317, 2, stride=1, padding=0)

    def forward(self, x0):
        y0 = self.conv_t(x0)
        y1 = (y0 > 0)
        y2 = (y0 * (- 0.26))
        y3 = torch.where(y1, y0, y2)
        return y3




func = Model().to('cuda')



x0 = torch.randn(3, 242)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [3, 242]

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(3, 242)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [3, 242]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''