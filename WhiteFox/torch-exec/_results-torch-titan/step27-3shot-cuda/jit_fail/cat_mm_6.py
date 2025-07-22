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

    def forward(self, x1, x2):
        x1 = torch.randn_like(x2).transpose((- 1), (- 2)).contiguous()
        v1 = (torch.nn.functional.interpolate(x1, mode='nearest', scale_factor=2) * (1.0 / torch.sqrt(2)))
        v2 = (torch.nn.functional.interpolate(x1, mode='nearest', scale_factor=0.1) * (1.0 / torch.sqrt(2)))
        return torch.cat([v1, v1, v2, v2], 2).contiguous()




func = Model().to('cuda')



x1 = torch.randn(2, 2, 2)



x2 = torch.randn(2, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
sqrt(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method sqrt of type object at 0x707fef8699e0>(*(2,), **{}):
sqrt(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''