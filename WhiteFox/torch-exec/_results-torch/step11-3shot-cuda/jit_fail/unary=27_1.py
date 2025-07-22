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

    def __init__(self, shape):
        super().__init__()
        self.conv = torch.nn.Conv2d(17, 10, 7, stride=4, padding=5)
        self.shape = shape

    def forward(self, input):
        v1 = self.conv(input)
        v2 = v1.view(*self.shape)
        return v2


shape = [1, 10, 20]

func = Model(shape).to('cuda')


input = torch.randn(1, 17, 32, 25)

test_inputs = [input]

# JIT_FAIL
'''
direct:
shape '[1, 10, 20]' is invalid for input of size 720

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 10, 9, 8)), 1, 10, 20), **{}):
shape '[1, 10, 20]' is invalid for input of size 720

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''