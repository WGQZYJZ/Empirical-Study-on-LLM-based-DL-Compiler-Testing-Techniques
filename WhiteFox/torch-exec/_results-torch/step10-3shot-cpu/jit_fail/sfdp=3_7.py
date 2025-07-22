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

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.mul(SCALE_FACTOR)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=DROPOUT_P)
        output = dropout_qk.matmul(x2)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 1, 512)

x2 = torch.randn(1, 1, 512)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'SCALE_FACTOR' is not defined

jit:
NameError: name 'SCALE_FACTOR' is not defined

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''