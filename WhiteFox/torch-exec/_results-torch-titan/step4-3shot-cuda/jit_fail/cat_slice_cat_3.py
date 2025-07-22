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
        v2 = v1[:, (- 1)]
        v3 = v2[0:1]
        v4 = torch.cat([v1, v3], dim=1)
        return __out__



func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)



x2 = torch.randn(1, 2, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 4 and 3

jit:
name '__out__' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''