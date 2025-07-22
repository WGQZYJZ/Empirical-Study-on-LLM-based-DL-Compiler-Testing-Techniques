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

    def forward(self, q, k, v, scale, dropout_p):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(scale)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



__q__ = torch.randn(3, 4, 32)



__k__ = torch.randn(3, 4, 64)



__v__ = torch.randn(3, 4, 64)



scale = float((2 ** 0.5))

q = 1

test_inputs = [__q__, __k__, __v__, scale, q]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 32] but got: [3, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x75aaa4c699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 4, 32)), FakeTensor(..., device='cuda:0', size=(3, 64, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 32] but got: [3, 64].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''