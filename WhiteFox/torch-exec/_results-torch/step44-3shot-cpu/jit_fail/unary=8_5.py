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
        self.conv_transpose = torch.nn.ConvTranspose1d(6, 2, 3, stride=3, padding=1, output_padding=0, groups=2, bias=False)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 6, 21, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 6, 21, 28]

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x78a6dc996ec0>(*(FakeTensor(..., size=(1, 6, 21, 28)), Parameter(FakeTensor(..., size=(6, 1, 3), requires_grad=True)), None, (3,), (1,), (0,), 2, (1,)), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 6, 21, 28]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''