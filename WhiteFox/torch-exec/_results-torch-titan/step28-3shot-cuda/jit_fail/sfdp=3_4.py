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

    def __init__(self, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, query, key, value, scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = F.softmax(scaled_qk, dim=(- 1))
        dropout_qk = F.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output




dropout_p = 0.5

func = Model(dropout_p).to('cuda')



b = 1


query = torch.randn(b, 1, 28, 28)



b = 1


key = torch.randn(b, 4, 14, 14)



b = 1


value = torch.randn(b, 4, 14, 14)

scale_factor = 1

test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 28] but got: [4, 14].

jit:
Failed running call_function <built-in method matmul of type object at 0x797fcd6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 28, 28)), FakeTensor(..., device='cuda:0', size=(1, 4, 14, 14))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 28] but got: [4, 14].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''