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
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = v1.div(10.0)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=0.1)
        v5 = v4.matmul(x2)
        return v5



func = Model().to('cuda')



x1 = torch.randn(2, 4, 5)



x2 = torch.randn(2, 5, 10)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 10].

jit:
Failed running call_function <built-in method matmul of type object at 0x7605fd4699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 4, 5)), FakeTensor(..., device='cuda:0', size=(2, 10, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 10].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''