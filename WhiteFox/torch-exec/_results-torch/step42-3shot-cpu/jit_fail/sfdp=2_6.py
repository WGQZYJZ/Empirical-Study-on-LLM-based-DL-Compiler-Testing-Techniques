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
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = softmax_qk.matmul(x3)
        return output


func = Model().to('cpu')


x1 = torch.randn(6, 25, 12)

x2 = torch.randn(6, 12, 64)

x3 = torch.randn(6, 64, 25)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [6, 12] but got: [6, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x707aec796ec0>(*(FakeTensor(..., size=(6, 25, 12)), FakeTensor(..., size=(6, 64, 12))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [6, 12] but got: [6, 64].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''