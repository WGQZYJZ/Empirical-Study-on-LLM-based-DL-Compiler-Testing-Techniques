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

    def forward(self, x1, x2, x3):
        v1 = [None]
        for i1 in range({1}):
            v1.insert(i1, x1)
        v2 = torch.cat(v1, dim=1)
        v3 = v2[:, 0:9223372036854775807]
        v4 = v3[:, 0:x2]
        v5 = torch.cat([v2, v4], dim=1)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)

x2 = 1
x3 = 1

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
'set' object cannot be interpreted as an integer

jit:
'set' object cannot be interpreted as an integer

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''