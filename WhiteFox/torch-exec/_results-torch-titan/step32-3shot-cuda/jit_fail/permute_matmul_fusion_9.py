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
        v0 = x2.permute(0, 2, 1)
        v1 = x1.permute(0, 2, 1)
        v2 = torch.matmul(v0, v1)
        v3 = torch.bmm(v1[(..., 0)], v0[(..., 1)])
        v4 = torch.cat((v2, v3), 1)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
batch1 must be a 3D tensor

jit:
Failed running call_function <built-in method bmm of type object at 0x70904b6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2)), FakeTensor(..., device='cuda:0', size=(1, 2))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''