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

    def forward(self, x1, x2):
        v1 = x1.permute(0, 1, 3, 2)
        v2 = torch.bmm(v1, x2)
        v3 = torch.matmul(v2, v1)
        return v3




func = Model1().to('cuda')



x1 = torch.randn(1, 1, 2, 3)



x2 = torch.randn(1, 1, 2, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
batch1 must be a 3D tensor

jit:
Failed running call_function <built-in method bmm of type object at 0x737ed6e699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 3, 2)), FakeTensor(..., device='cuda:0', size=(1, 1, 2, 3))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''