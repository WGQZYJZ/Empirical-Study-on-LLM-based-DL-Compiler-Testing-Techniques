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

    def __init__(self, min_value=2, max_value=3):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose3d(1, 64, 1, stride=1, padding=0, bias=False)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 1, 1, 1, 1, 201)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 4D (unbatched) or 5D (batched) input to conv_transpose3d, but got input of size: [1, 1, 1, 1, 1, 201]

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x74cecb196ec0>(*(FakeTensor(..., size=(1, 1, 1, 1, 1, 201)), Parameter(FakeTensor(..., size=(1, 64, 1, 1, 1), requires_grad=True)), None, (1, 1, 1), (0, 0, 0), (0, 0, 0), 1, (1, 1, 1)), **{}):
Expected 4D (unbatched) or 5D (batched) input to conv_transpose3d, but got input of size: [1, 1, 1, 1, 1, 201]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1347, in forward
    return F.conv_transpose3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''