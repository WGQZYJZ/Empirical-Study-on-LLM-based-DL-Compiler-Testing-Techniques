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

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')

x1 = 1
x2 = 1
x3 = 1
x4 = 1
x5 = 1
x6 = 1
x7 = 1
x8 = 1
x9 = 1
x10 = 1
x11 = 1
x12 = 1
x13 = 1
x14 = 1
x15 = 1

test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 60] but got: [4, 3].

jit:
Failed running call_function <built-in method matmul of type object at 0x7a0d2de699e0>(*(FakeTensor(..., size=(4, 3, 60)), FakeTensor(..., size=(4, 3, 120))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 60] but got: [4, 3].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''