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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(2, 4, 1, stride=2, padding=1, groups=2)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



x = torch.randn(1, 14, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=2, weight of size [4, 1, 1], expected input[1, 14, 64] to have 2 channels, but got 14 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 14, 64)),), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''