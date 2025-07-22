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
        self.dropout_p = 0.1

    def forward(self, __input0__, __input1__):
        qk = torch.matmul(__input0__, __input1__.transpose((- 2), (- 1)))
        scale_factor = (1.0 / math.sqrt(__input0__.shape[(- 1)]))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(__input1__)
        return output



func = Model().to('cuda')



__x0__ = torch.randn(1, 12, 512, 64)



__x1__ = torch.randn(1, 12, 64, 512)


test_inputs = [__x0__, __x1__]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [12, 64] but got: [12, 512].

jit:
Failed running call_function <built-in method matmul of type object at 0x7406076699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 12, 512, 64)), FakeTensor(..., device='cuda:0', size=(1, 12, 512, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [12, 64] but got: [12, 512].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''