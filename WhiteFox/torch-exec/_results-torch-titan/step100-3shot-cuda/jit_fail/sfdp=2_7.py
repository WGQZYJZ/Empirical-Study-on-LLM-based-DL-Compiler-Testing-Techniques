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

    def forward(self, x1, x2, dropout_p):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        inv_scale_factor = torch.sqrt(torch.tensor(32.0, dtype=x1.dtype, device=device).float())
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x2)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 256, 64)



x2 = torch.randn(1, 512, 64)

dropout_p = 1

test_inputs = [x1, x2, dropout_p]

# JIT_FAIL
'''
direct:
name 'device' is not defined

jit:
name 'device' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''