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
        self.query = torch.nn.Parameter(torch.zeros([4, 5, 10], dtype=torch.float), requires_grad=True)
        self.key = torch.nn.Parameter(torch.zeros([4, 6, 12], dtype=torch.float, requires_grad=True))
        self.value = torch.nn.Parameter(torch.zeros([4, 6, 20], dtype=torch.float, requires_grad=True))
        self.scale_factor = 10

    def forward(self, k1):
        qk = torch.matmul(self.query, self.key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5, training=True)
        output = dropout_qk.matmul(self.value)
        return output



func = Model().to('cuda')



k1 = torch.randn(2, 4, 5, 10)


test_inputs = [k1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 10] but got: [4, 12].

jit:
Failed running call_function <built-in method matmul of type object at 0x7949af0699e0>(*(Parameter(FakeTensor(..., device='cuda:0', size=(4, 5, 10), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(4, 12, 6), requires_grad=True)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 10] but got: [4, 12].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''