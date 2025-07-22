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
        x3 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        x4 = (x3 * 1.0)
        x5 = x4.softmax(dim=(- 1))
        x6 = torch.nn.functional.dropout(x5, p=0.1)
        v1 = torch.matmul(x6, x2)
        return v1



func = Model().to('cuda')



x1 = torch.randn(7, 12, 32)



x2 = torch.randn(7, 6, 48)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [7, 32] but got: [7, 48].

jit:
Failed running call_function <built-in method matmul of type object at 0x77099e2699e0>(*(FakeTensor(..., device='cuda:0', size=(7, 12, 32)), FakeTensor(..., device='cuda:0', size=(7, 48, 6))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [7, 32] but got: [7, 48].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''