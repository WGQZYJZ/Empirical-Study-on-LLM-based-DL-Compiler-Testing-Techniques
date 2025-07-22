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

    def __init__(self, hidden_size, num_heads):
        super().__init__()
        self.mha_layer_norm = torch.nn.LayerNorm(hidden_size)
        self.mha_attn_dropout = 0.1
        bias = True
        self.mha = torch.nn.MultiheadAttention(hidden_size, num_heads, bias=bias)

    def forward(self, input_tensor, attention_mask):
        attention_mask = torch.cat((input_tensor.new_zeros(input_tensor.size(0), 1, input_tensor.size(1)), input_tensor.new_ones(input_tensor.size(0), attention_mask.size(1) - 1, input_tensor.size(1))), 1)
        attention_mask = (1.0 - attention_mask) * -10000000.0
        attention_mask = attention_mask.unsqueeze(1)
        output = self.mha_layer_norm(input_tensor)
        (output, output_weights) = self.mha(output, output, output, attention_mask=attention_mask)
        output = output.transpose(0, 1).contiguous().view(input_tensor.size(1), -1)
        return output


hidden_size = 1
num_heads = 1

func = Model(hidden_size, num_heads).to('cpu')


input_tensor = torch.randn(4, 10, 100)

attention_mask = torch.rand(4, 10)

test_inputs = [input_tensor, attention_mask]

# JIT_FAIL
'''
direct:
Given normalized_shape=[1], expected input with shape [*, 1], but got input of size[4, 10, 100]

jit:
Failed running call_function <function layer_norm at 0x7820a3d71040>(*(FakeTensor(..., size=(4, 10, 100)), (1,), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), 1e-05), **{}):
Given normalized_shape=[1], expected input with shape [1], but got input of size torch.Size([4, 10, 100])

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/normalization.py", line 217, in forward
    return F.layer_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''