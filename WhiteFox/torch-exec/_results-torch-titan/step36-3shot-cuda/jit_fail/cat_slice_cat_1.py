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

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
        v1 = torch.cat([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10], dim=1)




func = Model().to('cuda')

x1 = 1
x2 = 1
x3 = 1
x4 = 1
x5 = 1
x6 = 1
x7 = 1
x8 = 1
x9 = 1
x10 = 1

test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x71ae076699e0>(*([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],), **{'dim': 1}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''