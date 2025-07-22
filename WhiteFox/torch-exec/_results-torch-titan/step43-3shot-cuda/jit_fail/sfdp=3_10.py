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

    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        scale_factor = (1 / math.sqrt(8))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)
        output = dropout_qk.matmul(x3)
        return output



func = Model().to('cuda')



x1 = torch.randn(8, 4, 10)



x2 = torch.randn(8, 7, 4)



x3 = torch.randn(8, 4, 7)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 10] but got: [8, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x79e12f0699e0>(*(FakeTensor(..., device='cuda:0', size=(8, 4, 10)), FakeTensor(..., device='cuda:0', size=(8, 4, 7))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 10] but got: [8, 4].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''