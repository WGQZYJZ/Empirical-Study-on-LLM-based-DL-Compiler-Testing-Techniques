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
        self.dropout = torch.nn.Dropout(p=0.1)

    def forward(self, query, key, value, attn_mask):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(2048.0)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(128, 4, 1024)



key = torch.randn(128, 1024, 512)



value = torch.randn(128, 1024, 512)



attn_mask = torch.randn(128, 5, 32)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [128, 1024] but got: [128, 512].

jit:
Failed running call_function <built-in method matmul of type object at 0x7ebc8fc699e0>(*(FakeTensor(..., device='cuda:0', size=(128, 4, 1024)), FakeTensor(..., device='cuda:0', size=(128, 512, 1024))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [128, 1024] but got: [128, 512].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''