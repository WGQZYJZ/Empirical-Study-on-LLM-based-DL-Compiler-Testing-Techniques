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

    def forward(self, x1, x2, x3, x4):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(10.0)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dp_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        return torch.matmul(dp_qk, x3)



func = Model().to('cuda')



x1 = torch.randn(1, 100, 2)



x2 = torch.randn(1, 2, 100)



x3 = torch.randn(1, 100, 50)



x4 = torch.randn(1, 100, 30)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 100].

jit:
Failed running call_function <built-in method matmul of type object at 0x770a20c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 100, 2)), FakeTensor(..., device='cuda:0', size=(1, 100, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 100].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''