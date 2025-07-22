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

    def forward(self, query, key, value, scale_factor=None, dropout_p=None):
        qk = torch.matmul(query, key.transpose((- 2), (- 1))).mul(scale_factor)
        softmax_qk = qk.softmax(dim=(- 1)).mul(dropout_p)
        dropout_qk = softmax_qk.matmul(value)
        return dropout_qk



func = Model().to('cuda')



query = torch.randn(1, 1, 3, 8)



key = torch.randn(1, 8, 20, 4)



value = torch.randn(1, 8, 20, 8)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 8] but got: [8, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x7043d04699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 3, 8)), FakeTensor(..., device='cuda:0', size=(1, 8, 4, 20))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 8] but got: [8, 4].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''