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



class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scale_factor = torch.tensor((1.0 / np.sqrt(key.shape[(- 1)])), dtype=query.dtype, device=query.device)
        softmax_qk = (qk * scale_factor).softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(value)
        return output



func = Model1().to('cuda')



value = torch.randn(1, 8, 23, 100)



key = torch.randn(1, 8, 23, 200)



query = torch.randn(1, 8, 20, 200)


test_inputs = [value, key, query]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 100] but got: [8, 200].

jit:
Failed running call_function <built-in method matmul of type object at 0x794dac8699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 23, 100)), FakeTensor(..., device='cuda:0', size=(1, 8, 200, 23))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 100] but got: [8, 200].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''