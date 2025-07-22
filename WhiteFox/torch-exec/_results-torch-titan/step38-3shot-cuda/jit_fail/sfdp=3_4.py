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

    def forward(self, x1, x2, x3, x4, x5):
        v1 = torch.matmul(x1, x2.permute(0, 1, 3, 2))
        v2 = (v1 * x3)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, x4)
        v5 = v4.matmul(x5)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 4, 8, 6)



x2 = torch.randn(1, 4, 6, 8)



x3 = torch.randn(1)



x4 = torch.randn(1)



x5 = torch.randn(1, 7, 2)


test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 6] but got: [4, 8].

jit:
Failed running call_function <built-in method matmul of type object at 0x7168e1a699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 8, 6)), FakeTensor(..., device='cuda:0', size=(1, 4, 8, 6))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 6] but got: [4, 8].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''