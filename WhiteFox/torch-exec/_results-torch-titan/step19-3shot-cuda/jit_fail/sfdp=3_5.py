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
        scale_factor = (1.0 / np.sqrt(query.shape[(- 1)]))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_p = 0.2
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 2, 10, 10)



key = torch.randn(1, 10, 20, 20)



value = torch.randn(1, 10, 20, 20)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (10) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x789cbbc699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 10, 10)), FakeTensor(..., device='cuda:0', size=(1, 10, 20, 20))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''