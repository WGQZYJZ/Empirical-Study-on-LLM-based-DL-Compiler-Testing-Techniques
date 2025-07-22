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

    def forward(self, query, key, value, dropout_p):
        inv_scale_factor = torch.sqrt(torch.tensor([(1.0 / query.size((- 1)))]))
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(16, 512, 32)



key = torch.randn(16, 512, 32)



value = torch.randn(16, 512, 32)

dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(16, 512, 512)), FakeTensor(..., size=(1,))), **{}):
Unhandled FakeTensor Device Propagation for aten.div.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''