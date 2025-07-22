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
        self.scale_factor = 0.7

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        output = softmax_qk.matmul(x2)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 16, 1024)

x2 = torch.randn(1, 16, 512)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 1024] but got: [1, 512].

jit:
Failed running call_function <built-in method matmul of type object at 0x79d8f0796ec0>(*(FakeTensor(..., size=(1, s2, s3)), FakeTensor(..., size=(1, s1, s0))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, s3] but got: [1, s1].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''