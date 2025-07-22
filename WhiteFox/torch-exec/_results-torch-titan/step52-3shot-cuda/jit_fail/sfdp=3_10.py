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



class Model(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, scale_factor=None, dropout_p=None, x3=None):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        if (scale_factor is not None):
            scaled_qk = qk.mul(scale_factor)
        else:
            scaled_qk = qk
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        if (dropout_p is not None):
            dropout_qk = nn.functional.dropout(softmax_qk, p=dropout_p)
        else:
            dropout_qk = softmax_qk
        if (x3 is not None):
            output = dropout_qk.matmul(x3)
        else:
            output = dropout_qk.matmul(x2)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 5, 3)



x2 = torch.randn(1, 5, 4)



x3 = torch.randn(1, 4, 5)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x77099e2699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 3)), FakeTensor(..., device='cuda:0', size=(1, 4, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 4].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''