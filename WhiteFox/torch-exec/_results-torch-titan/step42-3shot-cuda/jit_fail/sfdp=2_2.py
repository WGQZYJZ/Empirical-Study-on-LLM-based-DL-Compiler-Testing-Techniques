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



class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, q, k, v, scale_factor=None, inv_scale=None, dropout_p=0.0):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        if (scale_factor is not None):
            qk = qk.div(scale_factor.unsqueeze((- 1))).div(inv_scale.unsqueeze((- 1)).unsqueeze((- 2)))
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(v)



func = Model1().to('cuda')



__input_q__ = torch.randn(5, 20, 8)



__input_k__ = torch.randn(5, 8, 100)



__input_v__ = torch.randn(5, 50, 8)

q = 1
k = 1
v = 1

test_inputs = [__input_q__, __input_k__, __input_v__, q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [5, 8] but got: [5, 100].

jit:
Failed running call_function <built-in method matmul of type object at 0x76a0a1a699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 20, 8)), FakeTensor(..., device='cuda:0', size=(5, 100, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [5, 8] but got: [5, 100].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''