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

    def forward(self, input1, input2):
        QK = torch.matmul(query, key.transpose((- 2), (- 1)))
        v1 = QK.div(inv_scale_factor)
        v2 = v1.softmax(dim=(- 1))
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)
        v4 = v3.matmul(value)
        return v4



func = Model().to('cuda')

input1 = 1
input2 = 1

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
name 'query' is not defined

jit:
name 'query' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''