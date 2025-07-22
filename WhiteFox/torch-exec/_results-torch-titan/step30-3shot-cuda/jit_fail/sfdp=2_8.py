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

    def forward(self, *x):
        (q, k, v, inv_scale_factor, dropout_p) = x
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        y = dropout_qk.matmul(v)
        return y



func = Model().to('cuda')



shape = (1, 128, 256)


inv_scale_factor = torch.randn(shape)



shape = (1, 128, 256)


x1 = torch.randn(shape)



shape = (1, 128, 256)


x2 = torch.randn(shape)



shape = (1, 128, 256)


x3 = torch.randn(shape)


test_inputs = [inv_scale_factor, x1, x2, x3]

# JIT_FAIL
'''
direct:
not enough values to unpack (expected 5, got 4)

jit:


from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''