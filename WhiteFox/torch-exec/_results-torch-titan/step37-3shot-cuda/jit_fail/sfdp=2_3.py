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
        v1 = torch.matmul(x1, x2)
        v2 = torch.nn.functional.dropout(v1)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.matmul(v3, v1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(128, 60, 512)



x2 = torch.randn(128, 512, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [128, 3] but got: [128, 60].

jit:
Failed running call_function <built-in method matmul of type object at 0x71c34c0699e0>(*(FakeTensor(..., device='cuda:0', size=(128, 60, 3)), FakeTensor(..., device='cuda:0', size=(128, 60, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [128, 3] but got: [128, 60].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''