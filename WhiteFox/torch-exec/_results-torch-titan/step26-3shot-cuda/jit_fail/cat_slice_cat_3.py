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

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:2]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')

x1 = 1
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x7f389b8699e0>(*([1, 1],), **{'dim': 1}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''