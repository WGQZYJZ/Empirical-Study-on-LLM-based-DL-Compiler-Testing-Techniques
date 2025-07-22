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

    def forward(self, q1, k1):
        qk = torch.matmul(q1, k1.transpose(-2, -1))
        inv_scale_factor = 1 / np.sqrt(q1.shape[-1])
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=0.20000000298023224, training=self.training, inplace=False)
        output = dropout_qk.matmul(y1)
        return output


func = Model().to('cpu')



q1 = torch.randn(1, 128, 8, device='cpu', dtype=torch.double)


k1 = torch.randn(1, 128, 16, device='cpu', dtype=torch.double)

test_inputs = [q1, k1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 8] but got: [1, 16].

jit:
Failed running call_function <built-in method matmul of type object at 0x7550e2996ec0>(*(FakeTensor(..., size=(1, 128, 8), dtype=torch.float64), FakeTensor(..., size=(1, 16, 128), dtype=torch.float64)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 8] but got: [1, 16].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''