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
        self.conv_t = torch.nn.ConvTranspose2d(16, 192, 3, stride=2, padding=2, bias=False)

    def forward(self, x):
        v1 = self.conv_t(x)
        v2 = v1 > 0
        v3 = v1 * -0.481
        v4 = torch.where(v2, v1, v3)
        return torch.nn.functional.adaptive_avg_pool2d(v4, (1, 1))



func = Model().to('cpu')


x = torch.randn(1, 16, 128, 25, 30)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 16, 128, 25, 30]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x726da0396ec0>(*(FakeTensor(..., size=(1, 16, 128, 25, 30)), Parameter(FakeTensor(..., size=(16, 192, 3, 3), requires_grad=True)), None, (2, 2), (2, 2), (0, 0), 1, (1, 1)), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [1, 16, 128, 25, 30]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''