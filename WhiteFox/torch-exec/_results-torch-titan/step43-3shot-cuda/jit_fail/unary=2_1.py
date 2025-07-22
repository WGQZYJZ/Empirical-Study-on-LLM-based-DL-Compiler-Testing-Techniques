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
        self.conv_transpose = torch.nn.ConvTranspose1d(1, 1, (1, 3, 1), stride=(1, 2), padding=(0, 1, 1), dilation=(1, 2, 1))

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 * 0.5)
        v3 = ((v1 * v1) * v1)
        v4 = (v3 * 0.044715)
        v5 = (v1 + v4)
        v6 = (v5 * 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v2 * v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 1, 1, 456)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 1, 1, 456]

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 456)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 1, 1, 456]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''