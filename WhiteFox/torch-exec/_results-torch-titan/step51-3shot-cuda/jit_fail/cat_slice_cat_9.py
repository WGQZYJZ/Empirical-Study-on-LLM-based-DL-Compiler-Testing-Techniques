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
        v1 = [[x1, x2, x2, x2, x1, x1, x2, x1, x2, x1]]
        v2 = tensor.tensor(v1, dtype=x1.dtype)
        v3 = torch.cat(v2)
        v4 = v3[:, 0:9223372036854775807]
        v5 = v4[:, 0:v3.shape[1]]
        v6 = torch.cat((v3, v5))
        v8 = torch.nn.Conv2d(v6.shape[2], v6.shape[6], 1, stride=1)
        return v8(v6)



func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)



x2 = torch.randn(1, 3, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'tensor' is not defined

jit:
name 'tensor' is not defined

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''