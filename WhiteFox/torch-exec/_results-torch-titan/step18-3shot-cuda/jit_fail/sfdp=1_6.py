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
        self.key = torch.nn.Linear(4, 4)

    def forward(self, query, value1, value2, dropout_p):
        k = self.key(query)
        scaled_qk = torch.matmul(query, k.transpose((- 2), (- 1))).div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return (torch.matmul(dropout_qk, value1) + torch.matmul(softmax_qk.sub(dropout_qk), value2))



func = Model().to('cuda')



query = torch.randn(2, 4)



value1 = torch.randn(2, 2, 4)



value2 = torch.randn(2, 2, 4)

dropout_p = 1

test_inputs = [query, value1, value2, dropout_p]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'scale_factor'

jit:
scale_factor

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''