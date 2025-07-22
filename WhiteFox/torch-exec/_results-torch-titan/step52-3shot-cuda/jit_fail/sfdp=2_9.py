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

    def __init__(self, dim_q, dim_k, dim_v):
        super().__init__()
        self.query_linear = torch.nn.Linear(dim_q, dim_k)
        self.key_linear = torch.nn.Linear(dim_k, dim_k)
        self.value_linear = torch.nn.Linear(dim_v, dim_v)

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        q = self.query_linear(query)
        k = self.key_linear(key)
        v = self.value_linear(value)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output




dim_q = 16


dim_k = 18


dim_v = 20

func = Model(dim_q, dim_k, dim_v).to('cuda')



dim_q = 16


query = torch.randn(8, 3, dim_q)



dim_k = 18


key = torch.randn(8, 3, dim_k)



dim_v = 20


value = torch.randn(8, 3, dim_v)



inv_scale_factor = torch.randn(1)



dropout_p = torch.randn(1)


test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
dropout probability has to be between 0 and 1, but got tensor([-0.7862], device='cuda:0')

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpa7tu6_yw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpa7tu6_yw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpa7tu6_yw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''