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
        torch.manual_seed(0)
        self.conv = torch.nn.Conv2d(20, 20, 5)
        self.bn = torch.nn.BatchNorm2d(20, track_running_stats=False)

    def forward(self, x):
        return self.bn(self.conv(x))




func = Model().to('cuda')



x = torch.randn(1, 20, 5, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected more than 1 value per channel when training, got input size torch.Size([1, 20, 1, 1])

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 20, 1, 1)),), **{}):
Expected more than 1 value per channel when training, got input size torch.Size([1, 20, 1, 1])

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''