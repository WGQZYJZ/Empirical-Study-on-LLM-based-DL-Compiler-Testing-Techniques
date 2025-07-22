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

    def __init__(self, dim_k, dropout_p=0):
        super().__init__()
        self.dropout_p = dropout_p
        self.softmax = torch.nn.Softmax((- 1))
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, q, k, v, inv_scale_factor):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output




dim_k = 16

func = Model(dim_k, dropout_p).to('cuda')



dim_k = 16


q = torch.randn(1, 8, dim_k)



dim_k = 16


k = torch.randn(1, 7, dim_k)



dim_k = 16


v = torch.randn(1, 7, dim_k)

inv_scale_factor = 1

test_inputs = [q, k, v, inv_scale_factor]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpu9tpkaqs/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpu9tpkaqs', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpu9tpkaqs/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''