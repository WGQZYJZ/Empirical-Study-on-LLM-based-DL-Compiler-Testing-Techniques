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

    def forward(self, x, y):
        v1 = torch.matmul(x, y.transpose((- 2), (- 1)))
        v2 = (v1 * 3)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=0.25)
        v5 = torch.matmul(v4, x)
        return v5



func = Model().to('cuda')



x = torch.randn(1, 64, 2)



y = torch.randn(1, 2, 4)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x72fb154699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 2)), FakeTensor(..., device='cuda:0', size=(1, 4, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 4].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''