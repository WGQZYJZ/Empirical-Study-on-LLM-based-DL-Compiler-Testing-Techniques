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

    def __init__(self, scale_factor, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p
        self.scale_factor = scale_factor

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(x2)
        return output



scale_factor = 1
dropout_p = 1
func = Model(0.2, 0.3).to('cuda')



x1 = torch.randn(1, 8, 2)



x2 = torch.randn(1, 8, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 3].

jit:
Failed running call_function <built-in method matmul of type object at 0x7ebc8fc699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 2)), FakeTensor(..., device='cuda:0', size=(1, 3, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 3].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''