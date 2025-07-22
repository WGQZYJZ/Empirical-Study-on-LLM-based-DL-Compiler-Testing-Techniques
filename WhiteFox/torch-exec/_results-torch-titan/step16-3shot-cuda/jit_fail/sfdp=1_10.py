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

    def __init__(self, hidden_size):
        super().__init__()
        self.hidden_size = hidden_size

    def forward(self, hidden_states):
        q = hidden_states[:, :self.hidden_size]
        k = hidden_states[:, self.hidden_size:]
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = (k.size((- 2)) ** 0.5)
        qk = qk.div(inv_scale_factor)
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(v)
        return output



hidden_size = 1

func = Model(hidden_size).to('cuda')



x = torch.randn(1, 128, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_bmm)

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 1, 127)), FakeTensor(..., size=(1, 8, 2, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 127] but got: [8, 2].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''