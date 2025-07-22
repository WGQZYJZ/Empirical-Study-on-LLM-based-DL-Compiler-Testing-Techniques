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

    def __init__(self, min_value=-3.610921458183803, max_value=-2.613650681131714):
        super().__init__()
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(9, 12, 2, stride=2)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(12, 33, 1, stride=1)
        self.conv_transpose_3 = torch.nn.ConvTranspose1d(33, 8, 1, stride=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.conv_transpose_2(v1)
        v3 = self.conv_transpose_3(v2)
        v3_a = torch.clamp(v2, self.min_value, self.max_value)
        v3_b = torch.clamp(v3, self.min_value, self.max_value)
        return v3_b



func = Model().to('cpu')


x1 = torch.randn(1, 9, 11, 11)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 33, 22, 22]

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x7fe846196ec0>(*(FakeTensor(..., size=(1, 33, 22, 22)), Parameter(FakeTensor(..., size=(33, 8, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1,), (0,), (0,), 1, (1,)), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 33, 22, 22]

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''