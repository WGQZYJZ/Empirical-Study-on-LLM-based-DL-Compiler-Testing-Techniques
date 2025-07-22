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

    def forward(self, x1):
        a1 = torch.cat([x1, x1], 0)
        a2 = a1[:, 0:9223372036854775807]
        a3 = a2[:, 0:447]
        a4 = torch.cat([a1, a3], 1)
        return a4



func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x7b8ff90699e0>(*([1, 1], 0), **{}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''