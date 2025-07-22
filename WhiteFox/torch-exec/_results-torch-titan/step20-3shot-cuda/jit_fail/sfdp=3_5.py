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

    def forward(self, v1, v2):
        v3 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        v4 = v3.mul(12.77)
        v5 = v4.softmax(dim=(- 1))
        v6 = torch.nn.functional.dropout(v5, p=0.125)
        v7 = torch.matmul(v6, v2)
        return v7



func = Model().to('cuda')



v1 = torch.randn(1, 30, 256)



v2 = torch.randn(1, 256, 512)


test_inputs = [v1, v2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 512].

jit:
Failed running call_function <built-in method matmul of type object at 0x7fce800699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 30, 256)), FakeTensor(..., device='cuda:0', size=(1, 512, 256))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 512].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''