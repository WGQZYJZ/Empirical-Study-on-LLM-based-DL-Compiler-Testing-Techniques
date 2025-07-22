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

    def __init__(self, dim, dropout_rate=0.8, dropout_p=0.8853064031187673):
        super().__init__()
        self.dim = dim
        self.scale_factor = torch.nn.Parameter(torch.Tensor([(dim ** (- 0.5))]))
        self.dropout_rate = dropout_rate
        self.dropout_p = dropout_p
        self.q_matrix = torch.nn.Parameter(torch.Tensor(dim, dim))
        torch.nn.init.normal_(self.q_matrix)
        self.k_matrix = torch.nn.Parameter(torch.Tensor(dim, dim))
        torch.nn.init.normal_(self.k_matrix)
        self.v_matrix = torch.nn.Parameter(torch.Tensor(dim, dim))
        torch.nn.init.normal_(self.v_matrix)
        self.dropout = torch.nn.Dropout(dropout_rate)

    def forward(self, queries, keys, values):
        scale_factor = self.scale_factor.view(1, 1, 1)
        q_matrix = self.q_matrix.t().view(1, 1, self.dim, self.dim)
        k_matrix = self.k_matrix.t().view(1, 1, self.dim, self.dim)
        v_matrix = self.v_matrix.t().view(1, 1, self.dim, self.dim)
        qk = torch.matmul(queries, k_matrix).unsqueeze(2)
        scaled_qk = (qk * scale_factor).softmax((- 1))
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, v_matrix).squeeze(2)
        output = self.dropout(output)
        return output




dim = 128


func = Model(dim).to('cuda')



dim = 128


queries = torch.randn(1, dim)



dim = 128


keys = torch.randn(1, dim)



dim = 128


values = torch.randn(1, dim)


test_inputs = [queries, keys, values]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpd39378i9/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpd39378i9', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpd39378i9/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''