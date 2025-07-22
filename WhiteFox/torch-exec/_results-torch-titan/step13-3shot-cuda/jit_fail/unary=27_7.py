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
        self.conv1 = torch.nn.Conv2d(3, 1, 1)
        self.conv2 = torch.nn.Conv2d(1, 4, 1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.clamp_min(v1, min=0.45)
        v3 = torch.clamp_max(v2, min=0.26)
        v4 = self.conv2(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
clamp_max() received an invalid combination of arguments - got (Tensor, min=float), but expected one of:
 * (Tensor input, Tensor max, *, Tensor out)
 * (Tensor input, Number max, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_max of type object at 0x713413c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64)),), **{'min': 0.26}):
clamp_max() received an invalid combination of arguments - got (FakeTensor, min=float), but expected one of:
 * (Tensor input, Tensor max, *, Tensor out)
 * (Tensor input, Number max, *, Tensor out)


from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''