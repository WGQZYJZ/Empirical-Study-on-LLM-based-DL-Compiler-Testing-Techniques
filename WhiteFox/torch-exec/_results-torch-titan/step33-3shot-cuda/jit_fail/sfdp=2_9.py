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
        self.query = torch.nn.Linear(128, 128)
        self.key = torch.nn.Linear(128, 128)
        self.value = torch.nn.Linear(128, 128)

    def forward(self, x1, x2):
        qk = torch.matmul(x1, self.key(x2).transpose((- 2), (- 1)))
        scaled_qk = qk.div((2 ** 0.5))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.8)
        return self.value(x2).matmul(dropout_qk.transpose((- 2), (- 1)))



func = Model().to('cuda')



x1 = torch.randn(4, 128)



x2 = torch.randn(4, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x128 and 4x4)

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(4, 128)), FakeTensor(..., device='cuda:0', size=(4, 4))), **{}):
a and b must have same reduction dim, but got [4, 128] X [4, 4].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''