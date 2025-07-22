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

    def forward_helper(self, query_features, key_features, scale_factor, dropout_p):
        qk = torch.matmul(query_features, key_features.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

    def forward(self, q, k, v, dropout_p=0.0):
        if ((q.shape[2] % k.shape[2]) == 0):
            scale_factor = math.sqrt(k.shape[2])
        else:
            scale_factor = np.sqrt(k.shape[2])
        return self.forward_helper((q / scale_factor), k, scale_factor, dropout_p)



func = Model().to('cuda')



q = torch.randn(1, 23, 10000)



k = torch.randn(1, 768, 10000)



v = torch.randn(1, 768, 10000)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
name 'value' is not defined

jit:
name 'value' is not defined

from user code:
   File "<string>", line 33, in forward
  File "<string>", line 25, in forward_helper


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''