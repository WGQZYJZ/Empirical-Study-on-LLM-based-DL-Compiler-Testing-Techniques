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

    def forward(self, x1, x2, x3, x4):
        v1 = torch.cat((x1, x2))
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:x2.shape[1]]
        v4 = torch.cat((v1, v3))
        v5 = torch.cat((x3, x4), dim=1)
        v6 = v5[:, 0:9223372036854775807]
        v7 = v6[:, 0:x4.shape[1]]
        v8 = torch.cat((v5, v7), dim=1)
        v9 = torch.cat((v4, v8), dim=0)




func = Model().to('cuda')

x1 = 1
x2 = 1
x3 = 1
x4 = 1

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x711ab68699e0>(*((1, 1),), **{}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''