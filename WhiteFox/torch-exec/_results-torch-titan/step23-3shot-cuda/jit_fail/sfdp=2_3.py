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

    def forward(self, query, key, value, dropout_p, inv_scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 128, 160, 160)



key = torch.randn(1, 512, 40, 40)



value = torch.randn(1, 512, 40, 40)

dropout_p = 1
inv_scale_factor = 1

test_inputs = [query, key, value, dropout_p, inv_scale_factor]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (512) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x75aaa4c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 128, 160, 160)), FakeTensor(..., device='cuda:0', size=(1, 512, 40, 40))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''