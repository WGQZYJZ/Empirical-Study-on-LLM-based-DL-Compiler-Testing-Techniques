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
        inv_scale_factor = (1.0 / math.sqrt(query.size((- 1))))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(value)



func = Model().to('cuda')



query = torch.randn(5, 6, 7)



key = torch.randn(6, 8, 7)



value = torch.randn(6, 8, 9)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (6) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x7bd1b44699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 6, 7)), FakeTensor(..., device='cuda:0', size=(6, 7, 8))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''