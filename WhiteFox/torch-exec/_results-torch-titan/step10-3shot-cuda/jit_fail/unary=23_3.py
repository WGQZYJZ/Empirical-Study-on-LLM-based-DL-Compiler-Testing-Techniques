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



class MyModel(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.tanh(x1)
        v1 = torch.max_pool2d(v0, 2)
        v2 = torch.conv_transpose2d(v1, 4, 6, (4, 4))
        v3 = torch.max_pool2d(v2, 2)
        v4 = torch.conv2d(v3, 1, (3, 3))
        v5 = torch.tanh(v4)
        return v5




func = MyModel().to('cuda')



x1 = torch.randn(1, 4, 6, 6)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'weight' (position 2) must be Tensor, not int

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7aee258699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 3, 3)), 4, 6, (4, 4)), **{}):
conv_transpose2d(): argument 'weight' (position 2) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''