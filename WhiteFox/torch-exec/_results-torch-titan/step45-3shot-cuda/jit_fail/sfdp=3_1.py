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

    def forward(self, q, k, v):
        qk = (torch.matmul(q, k.transpose((- 2), (- 1))) * self.scale_factor)
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 80, 23, 34)



x2 = torch.randn(1, 5, 23, 34)



x3 = torch.randn(1, 5, 23, 34)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (80) must match the size of tensor b (5) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7a55970699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 80, 23, 34)), FakeTensor(..., device='cuda:0', size=(1, 5, 34, 23))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''