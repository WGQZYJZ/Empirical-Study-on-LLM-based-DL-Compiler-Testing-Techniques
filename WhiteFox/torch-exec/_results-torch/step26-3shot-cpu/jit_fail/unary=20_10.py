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
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=(11, 1), stride=(3, 2), padding=(1, 3))
        self.conv_transpose = torch.nn.ConvTranspose1d(1, 1, kernel_size=3, stride=3, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = torch.sigmoid(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 1, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 1, 8, 19]

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x7fc04bb96ec0>(*(FakeTensor(..., size=(1, 1, 8, 19)), Parameter(FakeTensor(..., size=(1, 1, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (3,), (2,), (0,), 1, (1,)), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 1, 8, 19]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''