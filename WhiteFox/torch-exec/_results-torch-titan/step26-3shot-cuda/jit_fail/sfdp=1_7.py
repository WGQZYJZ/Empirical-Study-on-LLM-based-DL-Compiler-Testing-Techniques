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

    def forward(self, query, key, value, scale_factor, dropout_p):
        q1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v1 = q1.div(scale_factor)
        v2 = v1.softmax(dim=(- 1))
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)
        output = v3.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(3, 1024, 256)



key = torch.randn(3, 1024, 256)



value = torch.randn(3, 2048, 256)



scale_factor = torch.randn(3, 256, 256)

dropout_p = 1

test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (1024) must match the size of tensor b (256) at non-singleton dimension 2

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(3, 1024, 1024)), FakeTensor(..., device='cuda:0', size=(3, 256, 256))), **{}):
Attempting to broadcast a dimension of length 256 at -1! Mismatching argument at index 1 had torch.Size([3, 256, 256]); but expected shape should be broadcastable to [3, 1024, 1024]

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''