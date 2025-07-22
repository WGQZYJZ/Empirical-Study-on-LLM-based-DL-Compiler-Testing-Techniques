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

    def __init__(self, num_heads=2):
        super().__init__()
        self.num_heads = num_heads
        self.w_q = torch.nn.Linear(16, (16 * num_heads), bias=False)
        self.w_k = torch.nn.Linear(24, (16 * num_heads), bias=False)
        self.w_v = torch.nn.Linear(32, (16 * num_heads), bias=False)
        self.projection = torch.nn.Linear((16 * num_heads), 16)

    def forward(self, q, k, v, inv_scale_factor, dropout_p):
        q = torch.stack([self.w_q(q) for _ in range(self.num_heads)], dim=1)
        k = torch.stack([self.w_k(k) for _ in range(self.num_heads)], dim=1)
        v = torch.stack([self.w_v(v) for _ in range(self.num_heads)], dim=1)
        qk = torch.matmul(q.transpose((- 2), (- 1)), k)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        output = output.transpose(1, 2)
        first_head = output[:, :, 0, :]
        logits = self.projection(first_head)
        return logits



func = Model().to('cuda')



q = torch.randn(1, 1, 16)



k = torch.randn(1, 4, 24)



v = torch.randn(1, 2, 32)



inv_scale_factor = torch.tensor([2.0])

dropout_p = 1

test_inputs = [q, k, v, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 1] but got: [2, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x75f6dda699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 32, 1)), FakeTensor(..., device='cuda:0', size=(1, 2, 4, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 1] but got: [2, 4].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''