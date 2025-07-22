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
        self.conv1 = torch.nn.Conv2d(3, 1, 7, stride=1, padding=3)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.transpose(v1, 1, 2)
        v3 = v2.reshape(1, 30400, 1024)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 513, 999)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 30400, 1024]' is invalid for input of size 512487

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 513, 1, 999)), 1, 30400, 1024), **{}):
shape '[1, 30400, 1024]' is invalid for input of size 512487

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''