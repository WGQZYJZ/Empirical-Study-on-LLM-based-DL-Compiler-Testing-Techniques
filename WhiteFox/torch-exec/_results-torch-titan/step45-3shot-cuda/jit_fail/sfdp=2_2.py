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
        self.matmul = torch.nn.Linear(16, 16)

    def forward(self, x1, x2):
        qk = self.matmul(x1)
        inv_scale_factor = x2.norm(2, 1).clamp(min=1e-12).reciprocal()
        softmax_qk = qk.div(inv_scale_factor).softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(x2)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 16)



x2 = torch.randn(8, 16)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(1, 16)), FakeTensor(..., device='cuda:0', size=(8,))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([8]); but expected shape should be broadcastable to [1, 16]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''