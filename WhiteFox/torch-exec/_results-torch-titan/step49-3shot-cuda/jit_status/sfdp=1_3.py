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



class FeedForward(torch.nn.Module):

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.ln1 = torch.nn.LayerNorm(128)
        self.ln2 = torch.nn.LayerNorm(128)
        self.dense1 = torch.nn.Linear(128, 256)
        self.dense2 = torch.nn.Linear(256, 128)
        self.dropout_p = 0.1
        self.dropout = torch.nn.Dropout(self.dropout_p)
        self.ff1 = FeedForward()

    def forward(self, query, key, value, inv_scale_factor):
        query = self.ln1(query)
        key = self.ln2(key)
        v1 = self.dense1(query)
        v2 = self.dense2(v1)
        v3 = self.dropout(v2)
        output = self.ff1(query, key, value, inv_scale_factor, self.dropout_p)
        return output



func = Model().to('cuda')



query = torch.randn(1, 256, 128)



key = torch.randn(1, 256, 128)



value = torch.randn(1, 256, 128)

inv_scale_factor = 1

test_inputs = [query, key, value, inv_scale_factor]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmppyd8_ncg/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmppyd8_ncg', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmppyd8_ncg/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''