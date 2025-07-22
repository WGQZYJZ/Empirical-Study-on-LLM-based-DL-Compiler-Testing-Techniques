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

    def forward(self, x1, x2):
        q = x1
        k = x2
        scale_factor = (1 / math.sqrt(k.size((- 1))))
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = (qk * scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = (dropout_qk * v)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 16, 512)



x2 = torch.randn(1, 16, 512)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 16)), FakeTensor(..., size=(8, 1, 2, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([8, 1, 2, 64]); but expected shape should be broadcastable to [1, 1, 16, 16]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''