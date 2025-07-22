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
        self.conv_t = torch.nn.ConvTranspose2d(428, 64, (47, 10), stride=1, padding=(46, 9), groups=1, bias=True)
        self.conv = torch.nn.Conv3d(16, 10, (3, 7, 3), stride=(1, 2, 2), padding=(1, 3, 1), dilation=(1, 1, 1), groups=1, bias=True)

    def forward(self, x):
        v1 = self.conv_t(x)
        v2 = self.conv(v1)
        return v2



func = Model().to('cpu')


x = torch.randn(8, 16, 428, 117, 39)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [8, 16, 428, 117, 39]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x794efab96ec0>(*(FakeTensor(..., size=(8, 16, 428, 117, 39)), Parameter(FakeTensor(..., size=(428, 64, 47, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (1, 1), (46, 9), (0, 0), 1, (1, 1)), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [8, 16, 428, 117, 39]

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''