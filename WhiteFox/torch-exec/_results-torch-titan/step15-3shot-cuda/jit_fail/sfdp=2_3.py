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

    def forward(self, x1, x2, x3, x4):
        q11_q44 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        inv_scale_factor = (1 / 127.0)
        scaled_qk = q11_q44.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.8)
        o11_o33 = dropout_qk.matmul(x3)
        r11_r33 = dropout_qk.matmul(x4)
        return (o11_o33, r11_r33)



func = Model().to('cuda')



x1 = torch.randn(2, 3, 2)



x2 = torch.randn(2, 2, 4)



x3 = torch.randn(2, 3, 3)



x4 = torch.randn(2, 3, 3)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 2] but got: [2, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x790e2a8699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 2)), FakeTensor(..., device='cuda:0', size=(2, 4, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 2] but got: [2, 4].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''