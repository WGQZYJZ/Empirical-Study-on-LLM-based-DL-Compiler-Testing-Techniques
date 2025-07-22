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

    def __init__(self, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        inv_scale_factor = math.sqrt(x1.size((- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(x3)
        return output



dropout_p = 1

func = Model(dropout_p).to('cuda')



x1 = torch.randn(2, 512, 768)



x2 = torch.randn(256, 512, 768)



x3 = torch.randn(256, 768, 512)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (256) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x7e9ae46699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 512, 768)), FakeTensor(..., device='cuda:0', size=(256, 768, 512))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''