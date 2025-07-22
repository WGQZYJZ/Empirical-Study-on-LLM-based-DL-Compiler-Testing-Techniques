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

    def forward(self, query, key, value, dropout_p=0.0, inv_scale_factor=1.0):
        query = query.float()
        key = key.float()
        value = value.float()
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.div(inv_scale_factor)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, dropout_p)
        output = v4.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 3, 64, 64)



key = torch.randn(1, 3, 32, 32)



value = torch.randn(1, 3, 32, 32)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 64] but got: [3, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x7a75daa699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 64] but got: [3, 32].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''