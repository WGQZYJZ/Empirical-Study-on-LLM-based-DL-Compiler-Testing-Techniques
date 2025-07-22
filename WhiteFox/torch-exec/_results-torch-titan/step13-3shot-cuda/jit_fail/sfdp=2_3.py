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

    def __init__(self, dropout_prob):
        super().__init__()
        self.dropout_p = dropout_prob

    def forward(self, query, key, value, inv_scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



dropout_prob = 1
func = Model1(0.05).to('cuda')



query = torch.randn(32, 3, 64)



key = torch.randn(32, 3, 72)



value = torch.randn(32, 72, 32)



inv_scale_factor = torch.tensor(8.0, requires_grad=False)


test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [32, 64] but got: [32, 72].

jit:
Failed running call_function <built-in method matmul of type object at 0x743d384699e0>(*(FakeTensor(..., device='cuda:0', size=(32, 3, 64)), FakeTensor(..., device='cuda:0', size=(32, 72, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [32, 64] but got: [32, 72].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''