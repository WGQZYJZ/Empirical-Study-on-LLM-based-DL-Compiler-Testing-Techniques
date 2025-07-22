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

    def __init__(self, min_value=-9.662e+37, max_value=6.687e+37):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 4, 3, stride=2, padding=1)
        self.conv_transpose3d = torch.nn.ConvTranspose3d(2, 5, 3, stride=1, padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v0 = x1
        v1 = self.conv_transpose2d(v0)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = v3.contiguous(memory_format=torch.channels_last)
        v4 = self.conv_transpose3d(v4)
        return v4



func = Model().to('cuda')


x1 = torch.randn(6, 3, 76, 88, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [6, 3, 76, 88, 1]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x72af92996ec0>(*(FakeTensor(..., device='cuda:0', size=(6, 3, 76, 88, 1)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 4, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(4,), requires_grad=True)), (2, 2), (1, 1), (0, 0), 1, (1, 1)), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [6, 3, 76, 88, 1]

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''