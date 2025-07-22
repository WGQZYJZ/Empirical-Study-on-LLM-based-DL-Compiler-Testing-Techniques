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
        self.conv1 = torch.nn.Conv1d(3, 128, kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=True, padding_mode='zeros')
        self.conv2 = torch.nn.Conv1d(128, 512, kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=True, padding_mode='zeros')
        self.linear = torch.nn.Linear(((11 * 11) * 512), 1000)

    def forward(self, x1, x2):
        x = (x1 - x2)
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.linear(v2.view(v2.size(0), (- 1)))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 112, 112)



x2 = torch.randn(1, 3, 112, 112)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 3, 112, 112]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 112, 112)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 3, 112, 112]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''