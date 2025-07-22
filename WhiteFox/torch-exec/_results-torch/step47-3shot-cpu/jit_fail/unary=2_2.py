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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1024, 8, kernel_size=[3, 3], stride=(1, 1), padding=(1, 1), dilation=(1, 1))
        self.conv_transpose2 = torch.nn.ConvTranspose1d(8, 8, kernel_size=[2], stride=[2], padding=[0])

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2 * v2
        v5 = v4 * 0.044715
        v6 = v2 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v3 * v9
        return v10



func = Model().to('cpu')


x1 = torch.randn(1, 1024, 1, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 8, 1, 1]

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x710493196ec0>(*(FakeTensor(..., size=(1, 8, 1, 1)), Parameter(FakeTensor(..., size=(8, 8, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (2,), (0,), (0,), 1, (1,)), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 8, 1, 1]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''