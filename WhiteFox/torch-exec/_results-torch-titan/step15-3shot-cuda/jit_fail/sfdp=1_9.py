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
        self.softmax_qk = torch.nn.Softmax(dim=(- 1))
        self.dropout_qk = torch.nn.Dropout(p=0.1)

    def forward(self, q, k, v, inv_scale_factor):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax_qk(scaled_qk)
        dropout_qk = self.dropout_qk(softmax_qk)
        return dropout_qk.matmul(v)



func = Model().to('cuda')



q = torch.randn(1, 100, 2304)



k = torch.randn(1, 100, 4608)



v = torch.randn(1, 100, 4608)



inv_scale_factor = torch.randn((1, 1, 1, 768))


test_inputs = [q, k, v, inv_scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 2304] but got: [1, 4608].

jit:
Failed running call_function <built-in method matmul of type object at 0x70fda46699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 100, 2304)), FakeTensor(..., device='cuda:0', size=(1, 4608, 100))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 2304] but got: [1, 4608].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''