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

    def forward(self, query, key, value, dropout_p=0.5):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = 2
        dropout_qk = torch.nn.functional.dropout(qk.div(inv_scale_factor).softmax(dim=(- 1)), p=dropout_p)
        return dropout_qk.matmul(value)



func = Model().to('cuda')



query = torch.randn(2, 3, 16)



key = torch.randn(2, 3, 20)



value = torch.randn(2, 3, 20)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 16] but got: [2, 20].

jit:
Failed running call_function <built-in method matmul of type object at 0x703b652699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 16)), FakeTensor(..., device='cuda:0', size=(2, 20, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 16] but got: [2, 20].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''