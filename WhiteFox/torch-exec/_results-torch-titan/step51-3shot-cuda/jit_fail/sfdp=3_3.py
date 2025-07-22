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
        self.scale_factor = torch.nn.Parameter(torch.ones(1, 1, 1, 1))

    def forward(self, q, k, v, dropout_p=0.0):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 8, 64, 64)



k = torch.randn(1, 8, 32, 32)



v = torch.randn(1, 8, 32, 32)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 64] but got: [8, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x701cc6e699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 64] but got: [8, 32].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''