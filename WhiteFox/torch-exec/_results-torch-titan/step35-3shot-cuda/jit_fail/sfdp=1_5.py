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

    def forward(self, x1, x2, x3, x4):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        inv_scale = (1 / 0.070576)
        scaled_qk = (qk * inv_scale)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(x3)
        return output



func = Model().to('cuda')



x1 = torch.randn(4, 9, 85)



x2 = torch.randn(4, 85, 71)



x3 = torch.randn(4, 71, 117)



x4 = torch.randn(4, 117, 110)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 85] but got: [4, 71].

jit:
Failed running call_function <built-in method matmul of type object at 0x7272dc8699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 9, 85)), FakeTensor(..., device='cuda:0', size=(4, 71, 85))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 85] but got: [4, 71].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''