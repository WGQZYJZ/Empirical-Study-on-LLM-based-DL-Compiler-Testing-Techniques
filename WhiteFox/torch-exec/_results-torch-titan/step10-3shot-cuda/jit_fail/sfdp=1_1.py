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

    def __init__(self, num_attention_heads, input_shape):
        super().__init__()
        self.num_heads = num_attention_heads
        self.num_head_projections = 3
        self.input_shape = input_shape
        self.query = torch.nn.Parameter(torch.randn(self.num_heads, input_shape[0], self.num_head_projections), requires_grad=True)
        self.key = torch.nn.Parameter(torch.randn(self.num_heads, input_shape[0], self.num_head_projections), requires_grad=True)
        self.value = torch.nn.Parameter(torch.randn(self.num_heads, input_shape[0], self.num_head_projections), requires_grad=True)

    def forward(self, x1, dropout_p):
        inv_scale_factor = torch.sqrt(torch.tensor(input_shape[0]).float())
        q = torch.matmul(self.query, x1.transpose((- 1), (- 2))).view(self.num_heads, x1.shape[1], self.num_head_projections)
        k = torch.matmul(self.key, x1.transpose((- 1), (- 2))).view(self.num_heads, x1.shape[1], self.num_head_projections)
        v = torch.matmul(self.value, x1.transpose((- 1), (- 2))).view(self.num_heads, x1.shape[1], self.num_head_projections)
        qk = torch.matmul(q, k.transpose(0, 1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax((- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, v)
        output = output.view(output.shape[1], output.shape[2], output.shape[3]).transpose((- 1), (- 2))
        return output



num_attention_heads = 1
input_shape = 1
func = Model(4, [128, 512]).to('cuda')



x1 = torch.randn(8, 512, 128)

dropout_p = 1

test_inputs = [x1, dropout_p]

# JIT_FAIL
'''
direct:
'int' object is not subscriptable

jit:
'int' object is not subscriptable

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''