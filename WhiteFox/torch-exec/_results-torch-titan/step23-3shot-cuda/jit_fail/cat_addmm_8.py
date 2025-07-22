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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers1 = nn.Conv1d(10, 256, kernel_size=1)
        self.layers2 = nn.Conv2d(512, 1024, kernel_size=1)

    def forward(self, x):
        x = self.layers2(self.layers1(x))
        x = x.flatten(start_dim=2)
        x = x.flatten(start_dim=1)
        return x




func = Model().to('cuda')



x = torch.randn(2, 16, 10, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [2, 16, 10, 10]

jit:
Failed running call_module L__self___layers1(*(FakeTensor(..., device='cuda:0', size=(2, 16, 10, 10)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [2, 16, 10, 10]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''