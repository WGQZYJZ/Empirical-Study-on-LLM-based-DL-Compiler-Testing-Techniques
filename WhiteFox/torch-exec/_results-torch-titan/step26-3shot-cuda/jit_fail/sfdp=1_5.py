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
        self.query = torch.nn.Linear(768, 1)
        self.key = torch.nn.Linear(768, 1)
        self.value = torch.nn.Linear(768, 1)

    def forward(self, x1):
        q = self.query(x1)
        k = self.key(x1)
        v = self.value(x1)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(0.00440160646)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(v)



func = Model().to('cuda')



x1 = torch.randn(1, 768, 25)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (768x25 and 768x1)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(1, 768, 25)),), **{}):
a and b must have same reduction dim, but got [768, 25] X [768, 1].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''