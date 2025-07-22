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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value=1)
        v3 = torch.clamp_max(v2, max_value=(- 1))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
clamp_min() received an invalid combination of arguments - got (Tensor, min_value=int), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_min of type object at 0x75ad4ba699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 14, 14)),), **{'min_value': 1}):
clamp_min() received an invalid combination of arguments - got (FakeTensor, min_value=int), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''