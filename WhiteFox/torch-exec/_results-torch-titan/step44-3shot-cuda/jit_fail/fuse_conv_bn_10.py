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
        torch.manual_seed(1)
        self.layer = torch.nn.Sequential(torch.nn.Conv3d(3, 4, 2, bias=True), torch.nn.Conv3d(3, 5, 3, bias=False))

    def forward(self, x2):
        s = self.layer(x2)
        return s




func = Model().to('cuda')



x2 = torch.randn(1, 3, 4, 4, 4)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 3, 3, 3, 3], expected input[1, 4, 3, 3, 3] to have 3 channels, but got 4 channels instead

jit:
Failed running call_module L__self___layer_1(*(FakeTensor(..., device='cuda:0', size=(1, 4, 3, 3, 3)),), **{}):
Given groups=1, weight of size [5, 3, 3, 3, 3], expected input[1, 4, 3, 3, 3] to have 3 channels, but got 4 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''