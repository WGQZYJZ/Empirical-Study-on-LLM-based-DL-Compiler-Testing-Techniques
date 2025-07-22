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

    def forward(self, q, k, v, scale_factor=None, dropout_p=0):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = (qk.mul(scale_factor) if scale_factor else qk)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 5, 32)



k = torch.randn(1, 5, 64)



v = torch.randn(1, 5, 64)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 32] but got: [1, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x72af43e699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 32)), FakeTensor(..., device='cuda:0', size=(1, 64, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 32] but got: [1, 64].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''