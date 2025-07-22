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

    def forward(self, query, key, value, dropout_p, scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



__input0__ = torch.randn(2, 3, 4)



__input1__ = torch.randn(2, 4, 6)



__input2__ = torch.randn(2, 4, 8)



__input3__ = torch.rand(1)



__input4__ = torch.randint(32, (1,))


test_inputs = [__input0__, __input1__, __input2__, __input3__, __input4__]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 6].

jit:
Failed running call_function <built-in method matmul of type object at 0x74c328c699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 4)), FakeTensor(..., device='cuda:0', size=(2, 6, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 6].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''