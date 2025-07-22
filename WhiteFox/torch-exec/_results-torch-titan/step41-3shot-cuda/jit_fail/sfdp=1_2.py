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
        self.mat_mul = torch.nn.Linear(64, 64)

    def forward(self, x1, x2):
        v1 = self.mat_mul(x1)
        v2 = torch.matmul(v1, x2.transpose((- 2), (- 1)))
        v3 = v2.div(5.0)
        v4 = v3.softmax(dim=(- 1))
        v5 = torch.nn.functional.dropout(v4, p=0.1)
        return v5.matmul(x2)



func = Model().to('cuda')



x1 = torch.randn(1, 64)



x2 = torch.randn(3, 64, 48)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 64] but got: [3, 48].

jit:
Failed running call_function <built-in method matmul of type object at 0x7aca114699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 64)), FakeTensor(..., device='cuda:0', size=(3, 48, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 64] but got: [3, 48].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''