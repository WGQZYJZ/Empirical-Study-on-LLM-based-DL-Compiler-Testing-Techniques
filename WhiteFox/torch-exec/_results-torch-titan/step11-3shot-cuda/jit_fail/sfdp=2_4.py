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
        self.proj0 = torch.nn.Linear(80, (num_heads * 8))
        self.proj1 = torch.nn.Linear((num_heads * 8), (num_heads * 8))

    def scaled_dot_product_attention(self, q, k, v):
        inv_scale_factor = np.power(k.shape[(- 1)], (- 0.5))
        qk = torch.matmul(qk, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = F.softmax(scaled_qk, dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, v)
        return output

    def forward(self, x1):
        v1 = self.proj0(x1)
        qk = self.proj1(v1)
        v2 = self.scaled_dot_product_attention(qk, qk, qk)
        return v2



num_heads = 1
func = Model(8).to('cuda')



x1 = torch.randn(2, 80)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'qk' referenced before assignment

jit:
local variable 'qk' referenced before assignment
'''