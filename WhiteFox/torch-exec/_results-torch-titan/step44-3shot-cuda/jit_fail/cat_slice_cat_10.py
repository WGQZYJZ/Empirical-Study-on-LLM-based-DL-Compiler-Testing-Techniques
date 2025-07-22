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



class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.cat([x1 for _ in range(10)])
        v3 = v2[:, 0:9223372036854775807]
        v4 = v3[:, 0:64]




func = Model1().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x743fabc699e0>(*([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],), **{}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''