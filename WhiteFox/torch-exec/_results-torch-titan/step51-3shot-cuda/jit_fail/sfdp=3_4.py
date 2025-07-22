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

    def forward(self, query, key, value):
        scale_factor = (key.shape[(- 1)] / query.shape[(- 1)]).pow(0.25)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = F.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 8, 48)



key = torch.randn(1, 8, 96)



value = torch.randn(1, 8, 96)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
'float' object has no attribute 'pow'

jit:
'float' object has no attribute 'pow'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''