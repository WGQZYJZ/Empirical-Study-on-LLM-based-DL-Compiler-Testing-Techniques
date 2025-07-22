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

    def forward(self, query, key, value, dropout_p=0.1):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = torch.tensor((1 / (dim ** 0.25))).to(query.device)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(10, 3, 64, 64)



key = torch.randn(10, 3, 64, 64)



value = torch.randn(10, 3, 64, 64)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
name 'dim' is not defined

jit:
name 'dim' is not defined

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''