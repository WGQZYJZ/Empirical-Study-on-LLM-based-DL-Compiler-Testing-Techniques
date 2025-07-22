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

    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = ((v1 * 1) / sqrt(800))
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=0.2)
        v5 = torch.matmul(v4, x3)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 400, 800)



x2 = torch.randn(1, 800, 400)



x3 = torch.randn(1, 400, 800)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 800] but got: [1, 400].

jit:
Failed running call_function <built-in method matmul of type object at 0x79536ac699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 400, 800)), FakeTensor(..., device='cuda:0', size=(1, 400, 800))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 800] but got: [1, 400].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''