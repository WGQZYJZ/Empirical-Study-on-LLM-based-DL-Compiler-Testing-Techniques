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
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=2, kernel_size=(1, 9), stride=(1, 1), padding=(1, 1))
        self.conv_transpose = torch.nn.ConvTranspose1d(160, 3, stride=(1, 1), kernel_size=(160, 1), bias=False)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = self.relu(v2)
        return v3



func = Model().to('cuda')


x1 = torch.randn(1, 1, 50, 120)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 2, 52, 114]

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x7fcf82996ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 52, 114)), Parameter(FakeTensor(..., device='cuda:0', size=(160, 3, 160, 1), requires_grad=True)), None, (1, 1), (0,), (0,), 1, (1,)), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 2, 52, 114]

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''