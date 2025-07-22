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

    def forward(self, query, key, value, inv_scale_factor, dropout_p, attention_mask):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return (output * attention_mask)



func = Model().to('cuda')



query = torch.randn(32, 196, 1536)



key = torch.randn(32, 2048, 64)



value = torch.randn(32, 2048, 64)




attention_mask = torch.zeros(32, 196, 2048, dtype=torch.float32)

inv_scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, attention_mask, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [32, 1536] but got: [32, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x7c5e412699e0>(*(FakeTensor(..., device='cuda:0', size=(32, 196, 1536)), FakeTensor(..., device='cuda:0', size=(32, 64, 2048))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [32, 1536] but got: [32, 64].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''