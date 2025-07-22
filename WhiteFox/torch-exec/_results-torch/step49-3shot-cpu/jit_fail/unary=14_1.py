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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(3, 3, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 3, 64, 64, 64]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x78cad9996ec0>(*(FakeTensor(..., size=(1, 3, 64, 64, 64)), Parameter(FakeTensor(..., size=(3, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 3, 64, 64, 64]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''