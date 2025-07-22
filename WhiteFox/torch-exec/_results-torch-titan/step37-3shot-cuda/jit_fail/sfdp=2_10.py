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
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(4.0)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, 0.25)
        v1 = dropout_qk.matmul(x1)
        return v1



func = Model().to('cuda')



x1 = torch.randn(3, 5, 64)



x2 = torch.randn(3, 9, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 9] but got: [3, 5].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(3, 5, 9)), FakeTensor(..., device='cuda:0', size=(3, 5, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 9] but got: [3, 5].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''