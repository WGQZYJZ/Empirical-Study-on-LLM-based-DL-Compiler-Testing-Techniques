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

    def __init__(self, min_value=0.2, max_value=5.0):
        super().__init__()
        self.max_unpooling = torch.nn.MaxUnpool2d(1, 1)
        self.conv_transpose = torch.nn.ConvTranspose2d(9, 10, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1, x2):
        v1 = self.conv_transpose(x2)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.max_unpooling(v3, x1, 1)
        return v4




func = Model().to('cuda')




x1 = torch.zeros((1, 3, 32, 32), dtype=float)



x2 = torch.randn(1, 9, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
object of type 'int' has no len()

jit:
Failed running call_module L__self___max_unpooling(*(FakeTensor(..., device='cuda:0', size=(1, 10, 30, 30)), FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32), dtype=torch.float64), 1), **{}):
object of type 'int' has no len()

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''