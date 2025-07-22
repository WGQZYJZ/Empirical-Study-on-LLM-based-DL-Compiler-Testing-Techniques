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

    def __init__(self, num_features, dropout_p, num_heads, hidden_dims):
        super().__init__()
        self.num_features = num_features
        self.dropout_p = dropout_p
        self.num_heads = num_heads
        self.hidden_dims = hidden_dims
        self.qk_linear = torch.nn.Linear(self.num_features, self.num_features)
        self.v_linear = torch.nn.Linear(self.num_features, self.num_features)

    def forward(self, query, key, value, inv_scale_factor=None):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        if (inv_scale_factor is not None):
            qk = qk.div(inv_scale_factor)
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



num_features = 1
dropout_p = 1
num_heads = 1
hidden_dims = 1

func = Model(num_features, dropout_p, num_heads, hidden_dims).to('cuda')



x1 = torch.randn(4, 64, 128)



x2 = torch.randn(4, 256, 128)



x3 = torch.randn(4, 64, 128)

query = 1

test_inputs = [x1, x2, x3, query]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 256] but got: [4, 64].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(4, 64, 256)), FakeTensor(..., device='cuda:0', size=(4, 64, 128))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 256] but got: [4, 64].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''