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
        v3 = torch.cat([x2.reshape([2, 4, 8])], dim=1)
        v4 = v1[:, 0:3]
        v5 = v2[:, 0:size]
        v6 = torch.cat([v1, v3], dim=1)
        return v6



func = Model().to('cuda')



x1 = torch.randn(2, 8, 8)



x2 = torch.randn(2, 128, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
shape '[2, 4, 8]' is invalid for input of size 2048

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(2, 128, 8)), [2, 4, 8]), **{}):
shape '[2, 4, 8]' is invalid for input of size 2048

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''