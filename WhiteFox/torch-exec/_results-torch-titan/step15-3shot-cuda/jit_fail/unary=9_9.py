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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        a1 = torch.eq(1, 1)
        if (not a1):
            v2 = (v1 + a1)
        else:
            v2 = (v1 + 8)
        v3 = v2.clamp(min=0)
        v4 = v3.clamp(max=6)
        v5 = (v4 / 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
eq() received an invalid combination of arguments - got (int, int), but expected one of:
 * (Tensor input, Tensor other, *, Tensor out)
 * (Tensor input, Number other, *, Tensor out)


jit:
Failed running call_function <built-in method eq of type object at 0x75eccda699e0>(*(1, 1), **{}):
eq() received an invalid combination of arguments - got (int, int), but expected one of:
 * (Tensor input, Tensor other, *, Tensor out)
 * (Tensor input, Number other, *, Tensor out)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''