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
        self.inv_scale_factor = 1.06
        self.dropout_p = 0.5

    def forward(self, query, key, value, x1):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = (qk / self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 768, 784)



key = torch.randn(1, 784, 784)



value = torch.randn(1, 768, 768)



x1 = torch.randn(1, 768, 768)


test_inputs = [query, key, value, x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 784] but got: [1, 768].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 768, 784)), FakeTensor(..., device='cuda:0', size=(1, 768, 768))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 784] but got: [1, 768].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''