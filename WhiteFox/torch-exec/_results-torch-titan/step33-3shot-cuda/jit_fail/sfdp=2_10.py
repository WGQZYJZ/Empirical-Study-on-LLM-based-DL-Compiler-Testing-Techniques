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

    def forward(self, Q, K, V, seq_len, attention_mask=None, dropout_p=0.0):
        QK = torch.matmul(Q, K.transpose((- 2), (- 1)))
        inv_scale_factor = (seq_len ** (- 0.5))
        scaled_QK = QK.div(inv_scale_factor)
        softmax_QK = scaled_QK.softmax(dim=(- 1))
        if (dropout_p > 0):
            dropout_QK = torch.nn.functional.dropout(softmax_QK, p=dropout_p)
        else:
            dropout_QK = softmax_QK
        output = dropout_QK.matmul(V)
        return output



func = Model().to('cuda')



Q = torch.randn(2, 4, 5)



K = torch.randn(2, 5, 6)



V = torch.randn(2, 5, 6)




attention_mask = (torch.tril(torch.ones(2, 6, 6)) == 0).unsqueeze(1).unsqueeze(1)

seq_len = 1

test_inputs = [Q, K, V, attention_mask, seq_len]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 6].

jit:
Failed running call_function <built-in method matmul of type object at 0x7005396699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 4, 5)), FakeTensor(..., device='cuda:0', size=(2, 6, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 6].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''