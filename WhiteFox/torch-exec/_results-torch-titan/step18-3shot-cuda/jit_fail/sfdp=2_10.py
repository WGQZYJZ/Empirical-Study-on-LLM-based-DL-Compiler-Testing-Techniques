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

    def forward(self, q1, k2, v3, dropout_p1):
        scale_factor = torch.tensor(1.0)
        inv_scale_factor = torch.tensor(1.0)
        qk = torch.matmul(q1, k2.transpose((- 2), (- 1)))
        scaled_qk = (qk * scale_factor).div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p1)
        o4 = dropout_qk.matmul(v3)
        return o4



func = Model().to('cuda')



q1 = torch.randn(1, 3, 8, 8)



k2 = torch.randn(2, 3, 6, 6)



v3 = torch.randn(2, 3, 8, 6)

dropout_p1 = 1

test_inputs = [q1, k2, v3, dropout_p1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [6, 8] but got: [6, 6].

jit:
Failed running call_function <built-in method matmul of type object at 0x7cd9894699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 8, 8)), FakeTensor(..., device='cuda:0', size=(2, 3, 6, 6))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [6, 8] but got: [6, 6].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''