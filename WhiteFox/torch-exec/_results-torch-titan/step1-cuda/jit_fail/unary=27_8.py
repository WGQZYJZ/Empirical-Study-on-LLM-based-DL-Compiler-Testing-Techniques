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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1, bias=False)
        self.conv.weight.data = (torch.eye(8) * (- 0.0001))

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.clamp(input=v1, min=6380.7001953125)
        v3 = torch.clamp(input=v2, max=6380.13720703125)
        return v3



func = Model().to('cuda')



x = torch.eye(3, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [3, 3]

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(3, 3)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [3, 3]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''