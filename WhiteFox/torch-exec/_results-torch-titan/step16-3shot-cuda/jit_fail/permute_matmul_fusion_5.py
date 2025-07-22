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



class Model(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4, x5):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(2, 1, 0)
        v3 = torch.bmm(v1, v2)
        v4 = v3.permute(2, 1, 0)
        v5 = v4.permute(1, 0, 2)
        return torch.matmul(x3.permute(0, 2, 1), x4)



func = Model().to('cuda')



x1 = torch.randn(1, 1024, 64)



x2 = torch.randn(1, 64, 10)



x3 = torch.randn(1, 10, 20)



x4 = torch.randn(1, 32, 10)



x5 = torch.randn(1, 5, 3, 3)


test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 1024] but got: [10, 64].

jit:
Failed running call_function <built-in method bmm of type object at 0x789410e699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 1024)), FakeTensor(..., device='cuda:0', size=(10, 64, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 1024] but got: [10, 64].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''