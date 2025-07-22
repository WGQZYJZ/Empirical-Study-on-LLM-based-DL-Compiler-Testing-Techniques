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
        self.scale_factor = 0.2
        self.dropout_p = 0.5

    def forward(self, query, key, value):
        output = torch.matmul(query, key.transpose((- 2), (- 1)))
        softmax_qk = (output * self.scale_factor)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output



func = Model().to('cuda')



query = torch.randn(16, 1, 128)



key = torch.randn(16, 1, 256)



value = torch.randn(16, 256, 1)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [16, 128] but got: [16, 256].

jit:
Failed running call_function <built-in method matmul of type object at 0x7a55970699e0>(*(FakeTensor(..., device='cuda:0', size=(16, 1, 128)), FakeTensor(..., device='cuda:0', size=(16, 256, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [16, 128] but got: [16, 256].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''