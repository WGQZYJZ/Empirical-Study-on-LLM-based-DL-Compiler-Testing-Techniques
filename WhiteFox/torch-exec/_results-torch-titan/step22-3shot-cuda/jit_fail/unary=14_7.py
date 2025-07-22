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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(4, 4, 4, stride=4, padding=1)

    def forward(self, x2):
        v0 = x2.shape
        v1 = x2.reshape(736, 4)
        v2 = self.conv_transpose1(v1)
        v3 = torch.sigmoid(v2)
        v4 = (v2 * v3)
        v5 = v4.reshape(v0)
        return v5




func = Model().to('cuda')



x2 = torch.randn(1, 1, 20, 20)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
shape '[736, 4]' is invalid for input of size 400

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 1, 20, 20)), 736, 4), **{}):
shape '[736, 4]' is invalid for input of size 400

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''