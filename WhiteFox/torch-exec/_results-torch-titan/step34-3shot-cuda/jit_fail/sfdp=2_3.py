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
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(___)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(___, p=0.1)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(10, 16, 512)



key = torch.randn(20, 16, 64)



value = torch.randn(20, 16, 64)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (20) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x7eadf9c699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 16, 512)), FakeTensor(..., device='cuda:0', size=(20, 64, 16))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''