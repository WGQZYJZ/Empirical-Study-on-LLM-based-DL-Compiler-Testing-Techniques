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
        self.conv = torch.nn.Conv2d(1, 19, 1, stride=1, padding=0)
        self.conv2 = torch.nn.ConvTranspose1d(19, 10, 1, stride=1, padding=0)
        self.conv3 = torch.nn.ConvTranspose1d(10, 3, 2, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.9009688679024191
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = v7 * 0.5
        v9 = v7 * 0.7071067811865476
        v10 = torch.erf(v9)
        v11 = v10 + 1
        v12 = v8 * v11
        v13 = self.conv3(v12)
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 1, 57, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 19, 57, 8]

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x77b361d96ec0>(*(FakeTensor(..., size=(1, 19, 57, 8)), Parameter(FakeTensor(..., size=(19, 10, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), (1,), (0,), (0,), 1, (1,)), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 19, 57, 8]

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''