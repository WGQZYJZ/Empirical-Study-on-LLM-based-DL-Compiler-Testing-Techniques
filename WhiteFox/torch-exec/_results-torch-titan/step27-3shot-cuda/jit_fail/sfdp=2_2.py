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

    def forward(self, x1, x2, x3, x4):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = v1.div(x3)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=x4)
        v5 = torch.matmul(v4, x2)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 2, 3)



x2 = torch.randn(1, 2, 4)



x3 = torch.randn(3)

x4 = 1

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x725519a699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3)), FakeTensor(..., device='cuda:0', size=(1, 4, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 4].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''