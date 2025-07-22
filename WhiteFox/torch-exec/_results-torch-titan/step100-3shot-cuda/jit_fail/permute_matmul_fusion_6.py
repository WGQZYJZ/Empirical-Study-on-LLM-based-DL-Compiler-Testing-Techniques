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
        v1 = x1.permute(0, 2, 1)
        v2 = x1.permute(0, 2, 1)
        v3 = x1.permute(0, 2, 1)
        v4 = torch.bmm(v1, v2)
        v5 = torch.bmm(v3, v4)
        v6 = torch.bmm(v3, v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(4, 1, 7)



x2 = torch.randn(4, 10, 7)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 1] but got: [4, 7].

jit:
Failed running call_function <built-in method bmm of type object at 0x710ab48699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 7, 1)), FakeTensor(..., device='cuda:0', size=(4, 7, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 1] but got: [4, 7].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''