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
        super(Model, self).__init__()
        self.conv_t = torch.nn.ConvTranspose3d(14, 41, 2, stride=1, padding=0, bias=True)
        self.conv_t2 = torch.nn.ConvTranspose2d(330, 427, 4, stride=2, padding=1, bias=False)

    def forward(self, x16):
        x1 = self.conv_t(x16)
        x2 = x1 > 0
        x3 = x1 * -0.08
        x4 = torch.where(x2, x1, x3)
        return self.conv_t2(x4)



func = Model().to('cpu')


x16 = torch.randn(2, 14, 49, 84, 51)

test_inputs = [x16]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [2, 41, 50, 85, 52]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x73e8acf96ec0>(*(FakeTensor(..., size=(2, 41, 50, 85, 52)), Parameter(FakeTensor(..., size=(330, 427, 4, 4), requires_grad=True)), None, (2, 2), (1, 1), (0, 0), 1, (1, 1)), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [2, 41, 50, 85, 52]

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''