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

    def __init__(self, dropout_p, input_size, num_heads, head_size, output_size, scale_factor):
        super().__init__()
        self.linear1 = torch.nn.Linear(input_size, output_size)

    def forward(self, x1, x2):
        q = self.linear1(x1)
        k = self.linear1(x2)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = (1.0 / scale_factor)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output




dropout_p = 0.8


input_size = 128


num_heads = 4


head_size = 64


output_size = 256


scale_factor = 1.0

func = Model(dropout_p, input_size, num_heads, head_size, output_size, scale_factor).to('cuda')



x1 = torch.randn(1024, 128)



x2 = torch.randn(1024, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_bmm)

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1024, 1024)), FakeTensor(..., size=(1, 128, 768))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 1024] but got: [1, 128].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''