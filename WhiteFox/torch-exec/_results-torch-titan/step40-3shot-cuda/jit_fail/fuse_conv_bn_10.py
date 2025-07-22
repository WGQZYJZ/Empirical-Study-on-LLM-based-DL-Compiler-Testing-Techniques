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
        conv = torch.nn.Conv2d(3, 128, kernel_size=3)
        bn = torch.nn.BatchNorm2d(num_features=3)
        self.convbn = torch.nn.Sequential(conv, bn)

    def forward(self, x):
        output = self.convbn(x)
        return output




func = Model().to('cuda')



x1 = torch.randn(1, 3, 10, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 128 elements not 3

jit:
Failed running call_module L__self___convbn_1(*(FakeTensor(..., device='cuda:0', size=(1, 128, 8, 8)),), **{}):
running_mean should contain 128 elements not 3

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''