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
        self.conv = torch.nn.Conv2d(8, 8, 7, stride=1, padding=3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.transpose(v1, 1, 1)
        v3 = torch.inverse(v2)
        v4 = torch.triangular_solve(v3.contiguous(), torch.cholesky(v1.contiguous()))
        v5 = v4.solution
        v6 = torch.cholesky(v1.contiguous())
        v7 = torch.transpose(v1, 1, 1)
        v8 = torch.inverse(v2)
        v9 = torch.triangular_solve(v8.contiguous(), v6)
        v10 = v9.solution
        v11 = (v5 + 1)
        v12 = (v10 + 1)
        v13 = (v7 * v11)
        v14 = (v12 * v13)
        v15 = torch.bmm(v14, v14)
        return v14




func = Model().to('cuda')



x1 = torch.randn(1, 8, 112, 112)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
cholesky: (Batch element 0): The factorization could not be completed because the input is not positive-definite (the leading minor of order 1 is not positive-definite).

jit:
Failed running call_function <built-in method bmm of type object at 0x750afac699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 112, 112)), FakeTensor(..., device='cuda:0', size=(1, 8, 112, 112))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''