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
        a = x1.permute(0, 2, 1)
        b = x1.permute(1, 0, 2)
        c = x1.permute(1, 2, 0)
        d = x1.permute(2, 0, 1)
        e = x1.permute(2, 1, 0)
        v1 = c.permute(0, 2, 1)
        v2 = torch.bmm(d, e.permute(0, 2, 1))
        v3 = torch.matmul(a, v1)
        v4 = v3.permute(0, 2, 1).contiguous()
        return v4.detach()




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 2] but got: [2, 1].

jit:
Failed running call_function <built-in method bmm of type object at 0x753e1e8699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 1, 2)), FakeTensor(..., device='cuda:0', size=(2, 1, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 2] but got: [2, 1].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''