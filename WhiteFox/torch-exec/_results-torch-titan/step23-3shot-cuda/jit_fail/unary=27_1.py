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

    def __init__(self, axis, min_value=5, max_value=(- 5), keepdim=True):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.min_value = min_value
        self.max_value = max_value
        self.axis = axis
        self.keepdim = keepdim

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value, {'dim': self.axis, 'keepdim': self.keepdim})
        v3 = torch.clamp_max(v2, self.max_value, {'dim': self.axis, 'keepdim': self.keepdim})
        return v3




axis = 0


func = Model(axis).to('cuda')



x1 = torch.randn(1, 3, 52, 52)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
clamp_min() received an invalid combination of arguments - got (Tensor, int, dict), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_min of type object at 0x7da6166699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 52, 52)), 5, {'dim': 0, 'keepdim': True}), **{}):
clamp_min() received an invalid combination of arguments - got (FakeTensor, int, immutable_dict), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''