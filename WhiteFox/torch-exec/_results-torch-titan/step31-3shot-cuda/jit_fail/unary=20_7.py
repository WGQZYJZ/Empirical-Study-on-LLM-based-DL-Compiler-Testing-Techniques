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

    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(x1, None, kernel_size=(9, 9), stride=(2, 2), padding=(1, 1))
        v2 = torch.sigmoid(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 16, 14, 14)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'weight' (position 2) must be Tensor, not NoneType

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7d82eb4699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 14, 14)), None), **{'kernel_size': (9, 9), 'stride': (2, 2), 'padding': (1, 1)}):
conv_transpose2d(): argument 'weight' (position 2) must be Tensor, not NoneType

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''