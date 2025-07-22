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
        mm = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v1 = mm.div(0.1)
        v2 = v1.softmax(dim=(- 1))
        v3 = torch.nn.functional.dropout(v2, p=0.95)
        v4 = v3.matmul(x1)
        return (v3, v4)



func = Model().to('cuda')



x1 = torch.randn(1, 64, 32)



x2 = torch.randn(1, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 32] but got: [1, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x74c328c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 32)), FakeTensor(..., device='cuda:0', size=(1, 64, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 32] but got: [1, 64].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''