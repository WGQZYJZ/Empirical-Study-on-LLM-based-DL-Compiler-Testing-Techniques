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

    def forward(self, qk, qk_scaling_factor, query, key, value, p=0.0, is_training=False, epsilon=1e-06):
        input_dtype = query.dtype
        m = torch.matmul(query, key.transpose((- 2), (- 1)))
        qk = (m / torch_dtype_to_gain[input_dtype])
        qk = (qk / qk_scaling_factor)
        if is_training:
            qk = torch.nn.functional.dropout(qk, p, True, False)
        else:
            qk = torch.nn.functional.dropout(qk, p, False, False)
        o = torch.matmul(qk, value)
        return o



func = Model().to('cuda')



qk = torch.randn(1, 64, 10)



qk_scaling_factor = torch.randn(1, 1)



query = torch.randn(1, 512, 64)



key = torch.randn(1, 512, 1024)



value = torch.randn(1, 512, 1024)


test_inputs = [qk, qk_scaling_factor, query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 1024].

jit:
Failed running call_function <built-in method matmul of type object at 0x765a484699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 512, 64)), FakeTensor(..., device='cuda:0', size=(1, 1024, 512))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 1024].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''