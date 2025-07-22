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
        self.conv = torch.nn.Conv1d(2, 2, 1, stride=1, padding=1)

    def forward(self, x1):
        v = self.conv(x1)
        return v




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 2, 2, 2]

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 2, 2, 2]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''