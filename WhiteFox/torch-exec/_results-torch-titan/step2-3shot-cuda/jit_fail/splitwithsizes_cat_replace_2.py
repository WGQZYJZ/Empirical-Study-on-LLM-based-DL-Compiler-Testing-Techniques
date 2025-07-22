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
        self.convs = torch.nn.ModuleList([torch.nn.Conv2d(3, 8, 3, stride=2, padding=1), torch.nn.Conv2d(8, 8, 3, stride=1, padding=1)])

    def forward(self, x1):
        for conv in self.convs:
            x1 = conv(x1)
        (split_tensor1, split_tensor2) = torch.split(x1, [32, 48], dim=1)
        x2 = torch.cat((split_tensor1, split_tensor2), dim=1)
        x3 = torch.max(x1, dim=1)[0]
        return True



func = Model().to('cuda')



x1 = torch.randn(1, 128, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 128, 64, 64] to have 3 channels, but got 128 channels instead

jit:
Failed running call_module L__self___convs_0(*(FakeTensor(..., device='cuda:0', size=(1, 128, 64, 64)),), **{}):
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 128, 64, 64] to have 3 channels, but got 128 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''