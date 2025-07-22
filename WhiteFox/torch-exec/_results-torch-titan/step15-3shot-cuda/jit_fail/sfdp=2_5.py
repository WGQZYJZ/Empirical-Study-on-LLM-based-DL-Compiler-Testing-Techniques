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
        v2 = (v1 / 32)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=0.1, training=False)
        v5 = torch.matmul(v4, x2)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 32, 512)



x2 = torch.randn(1, 512, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 512] but got: [1, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x790e2a8699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 512)), FakeTensor(..., device='cuda:0', size=(1, 64, 512))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 512] but got: [1, 64].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''