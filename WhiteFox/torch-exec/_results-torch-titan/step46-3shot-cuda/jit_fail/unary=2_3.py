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
        self.conv_transpose = torch.nn.ConvTranspose3d(1, 11, (4, 1, 3), stride=1, padding=(3, 0, 1))
        self.avg_pool = torch.nn.AvgPool2d(3, stride=3)
        self.max_pool = torch.nn.MaxPool2d(3, stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.avg_pool(v1)
        v3 = self.max_pool(v2)
        return (0.2 * v3)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 4, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D or 4D (batch mode) tensor with optional 0 dim batch size for input, but got:[1, 11, 1, 4, 4]

jit:
Failed running call_module L__self___avg_pool(*(FakeTensor(..., device='cuda:0', size=(1, 11, 1, 4, 4)),), **{}):
Expected 3D or 4D (batch mode) tensor with optional 0 dim batch size for input, but got: torch.Size([1, 11, 1, 4, 4])

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''