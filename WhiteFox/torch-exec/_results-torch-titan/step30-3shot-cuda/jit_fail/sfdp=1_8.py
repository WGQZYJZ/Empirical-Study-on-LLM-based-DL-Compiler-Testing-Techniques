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

    def forward(self, query, key, value):
        v6 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v7 = v6.div(inv_scale_factor)
        v8 = v7.softmax(dim=(- 1))
        v9 = torch.nn.functional.dropout(v8, p=dropout_p)
        v10 = v9.matmul(value)
        return v10



func = Model().to('cuda')



query = torch.randn(3, 1024, 64)



key = torch.randn(3, 1024, 64)



value = torch.randn(3, 1024, 64)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(3, 1024, 1024)), FakeTensor(..., size=(1,))), **{}):
Unhandled FakeTensor Device Propagation for aten.div.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''