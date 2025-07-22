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

    def __init__(self, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.qkv_proj = torch.nn.Parameter(torch.randn((3 * num_heads), 128, 64))
        self.kv_proj = torch.nn.Parameter(torch.randn((2 * num_heads), 128, 64))
        self.output_proj = torch.nn.Parameter(torch.randn(num_heads, 128, 64))
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, qk):
        qk = torch.matmul(qk, self.qkv_proj)
        head_size = (qk.size(1) // self.num_heads)
        qk = qk.reshape(qk.size(0), (- 1), self.num_heads, head_size)
        q = qk[:, :, :, :head_size]
        k = qk[:, :, :, head_size:]
        k = torch.matmul(k, self.kv_proj)
        head_size = (k.size(1) // self.num_heads)
        k = k.reshape(k.size(0), (- 1), self.num_heads, head_size)
        v = k[:, :, :, head_size:]
        inv_scale_factor = (1 / math.sqrt(head_size))
        scaled_qk = qk.mul(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        output = output.reshape(output.size(0), (- 1), 128)
        output = torch.matmul(output, self.output_proj)
        output = output.div((1 / math.sqrt(head_size)))
        return output



num_heads = 1
func = Model(8).to('cuda')



qk = torch.randn(1, 384, 64)


test_inputs = [qk]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [24, 64] but got: [24, 128].

jit:
Failed running call_function <built-in method matmul of type object at 0x76a0a1a699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 384, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(24, 128, 64), requires_grad=True))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [24, 64] but got: [24, 128].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''