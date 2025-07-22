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

    def __init__(self, channels: int, num_heads: int):
        super().__init__()
        self.channels_size = channels
        self.head_size = (channels // num_heads)
        self.linear_q = torch.nn.Linear(channels, channels, bias=True)
        self.linear_k = torch.nn.Linear(channels, channels, bias=True)
        self.linear_v = torch.nn.Linear(channels, channels, bias=True)
        self.scaling_factor = np.sqrt(self.head_size)

    def forward(self, x1, x2, x3):
        q_vector = self.linear_q(x1)
        k_vector = self.linear_k(x2)
        v_vector = self.linear_v(x3)
        q_head = self.compute_qkv_head(q_vector)
        k_head = self.compute_qkv_head(k_vector)
        v_head = self.compute_qkv_head(v_vector)
        attention = torch.matmul(q_head, k_head.transpose((- 2), (- 1)))
        scaled_attention = attention.div(self.scaling_factor)
        softmax_attention = scaled_attention.softmax(dim=(- 1))
        dropout_attention = torch.nn.functional.dropout(softmax_attention, p=0.5)
        output = torch.matmul(dropout_attention, v_head)
        output = self.combine_heads(output)
        return output

    def compute_qkv_head(self, x: torch.Tensor):
        (batch_size, seq_length, _) = x.shape
        qkv_head = torch.reshape(x, (batch_size, seq_length, self.num_heads, self.head_size))
        qkv_head = torch.transpose(qkv_head, 1, 2)
        qkv_head = torch.reshape(qkv_head, (batch_size, self.num_heads, seq_length, self.head_size))
        return qkv_head

    def combine_heads(self, x: torch.Tensor):
        (batch_size, _, seq_length, _) = x.shape
        x = torch.transpose(x, 1, 2)
        x = torch.reshape(x, (batch_size, seq_length, self.channels_size))
        return x



channels = 1
num_heads = 1
func = Model(3, 2).to('cuda')



x1 = torch.randn(16, 3, 8)



x2 = torch.randn(16, 3, 8)



x3 = torch.randn(16, 3, 8)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (48x8 and 3x3)

jit:
Failed running call_module L__self___linear_q(*(FakeTensor(..., device='cuda:0', size=(16, 3, 8)),), **{}):
a and b must have same reduction dim, but got [48, 8] X [3, 3].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''