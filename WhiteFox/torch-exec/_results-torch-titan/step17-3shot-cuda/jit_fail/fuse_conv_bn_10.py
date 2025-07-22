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
        super(Model, self).__init__()
        self.layer = nn.Sequential(nn.Conv2d(6, 2, kernel_size=3, stride=2), nn.BatchNorm2d(6))

    def forward(self, x):
        return self.layer(x)




func = Model().to('cuda')



x = torch.randn(1, 6, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 2 elements not 6

jit:
Failed running call_module L__self___layer_1(*(FakeTensor(..., device='cuda:0', size=(1, 2, 1, 1)),), **{}):
running_mean should contain 2 elements not 6

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''