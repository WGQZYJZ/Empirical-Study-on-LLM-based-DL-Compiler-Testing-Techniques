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

    def forward(self, qk, inv_scale_factor):
        softmax_qk = self.dropout_qk(qk)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



qk = torch.randn(5, 10, 64, 64)



inv_scale_factor = torch.randn(1)


test_inputs = [qk, inv_scale_factor]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'dropout_qk'

jit:
dropout_qk

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''