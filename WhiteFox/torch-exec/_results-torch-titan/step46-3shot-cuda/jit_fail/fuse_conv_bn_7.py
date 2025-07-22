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
        self.fc = torch.nn.Linear(16, 16)
        self.conv = torch.nn.Conv3d(16, 16, (3, 3, 3))
        self.bn = torch.nn.BatchNorm3d(16)

    def forward(self, x):
        y = self.fc(x)
        y = self.conv(y)
        y = self.bn(y)
        return y




func = Model().to('cuda')



x = torch.randn(1, 16)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 16]

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 16)),), **{}):
Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 16]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''