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
        v2 = (v1 + 3)
        v3 = torch.clamp(v2, 0, None, 0)
        v4 = torch.clamp(v3, 6, None, 0)
        v5 = torch.div(v4, 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
clamp() received an invalid combination of arguments - got (Tensor, int, NoneType, int), but expected one of:
 * (Tensor input, Tensor min, Tensor max, *, Tensor out)
 * (Tensor input, Number min, Number max, *, Tensor out)


jit:
Failed running call_function <built-in method clamp of type object at 0x73fd2f6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), 0, None, 0), **{}):
clamp() received an invalid combination of arguments - got (FakeTensor, int, NoneType, int), but expected one of:
 * (Tensor input, Tensor min, Tensor max, *, Tensor out)
 * (Tensor input, Number min, Number max, *, Tensor out)


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''