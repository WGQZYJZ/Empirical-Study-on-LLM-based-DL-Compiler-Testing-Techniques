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
        self.conv_ = torch.nn.modules.conv.Conv1d(2, 2, 2)

    def forward(self, x1):
        v1 = self.conv_(x1)
        v2 = v1.permute(0, 1, 3, 2)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 2, 2, 2]

jit:
Failed running call_module L__self___conv_(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 2, 2, 2]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''