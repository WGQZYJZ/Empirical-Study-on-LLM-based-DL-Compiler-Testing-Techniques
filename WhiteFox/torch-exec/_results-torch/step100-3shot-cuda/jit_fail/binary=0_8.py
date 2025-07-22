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
        self.conv = torch.nn.Conv3d(3, 16, 3, padding=1)

    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other == None:
            other = torch.randn(v1.shape)
        v2 = torch.relu(v1 + other)
        return v2 if v2.size(3) == 8 and v2.size(2) == 8 else v2.sum(dim=(2, 3, 4))



func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, s1, s2, s3)), FakeTensor(..., size=(1, 16, s1, s2, s3))), **{}):
Tensor on device cpu is not on the expected device cuda:0!

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''