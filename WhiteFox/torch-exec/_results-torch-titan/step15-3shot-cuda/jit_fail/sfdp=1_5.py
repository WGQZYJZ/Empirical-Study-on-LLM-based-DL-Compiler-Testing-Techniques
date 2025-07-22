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
        self.query = torch.nn.Linear(128, 64, bias=False)
        self.key = torch.nn.Linear(128, 64, bias=False)
        self.value = torch.nn.Linear(128, 128, bias=False)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, x2):
        q = self.query(x2)
        k = self.key(x2)
        v = self.value(x2)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = torch.Tensor([10])
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v)
        return output



func = Model().to('cuda')



x2 = torch.randn(128, 128)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(128, 128)), FakeTensor(..., size=(1,))), **{}):
Unhandled FakeTensor Device Propagation for aten.div.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''