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

    def __init__(self, scale_factor=1, dropout_p=0, device='cpu'):
        super().__init__()

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = torch.tensor(self.scale_factor).to(self.device).inverse()
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(3, 2, 200)



key = torch.randn(3, 2, 500)



value = torch.randn(3, 2, 500)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 200] but got: [3, 500].

jit:
Failed running call_function <built-in method matmul of type object at 0x7299cd4699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 2, 200)), FakeTensor(..., device='cuda:0', size=(3, 500, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 200] but got: [3, 500].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''