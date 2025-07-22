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
        self.conv1 = torch.nn.Conv2d(3, 4, (3, 5), stride=(2, 3), padding=(1, 2))
        self.conv2 = torch.nn.Conv1d(3, 4, 5, stride=3, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = torch.relu((v1 + v2))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 3, 64, 64]

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 3, 64, 64]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''