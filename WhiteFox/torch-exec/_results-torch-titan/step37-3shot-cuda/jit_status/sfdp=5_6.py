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

    def __init__(self):
        super().__init__()
        self.dropout = 0.1
        self.heads = 4
        self.seq_len = 64
        self.dim = (16 // self.heads)
        self.head_dim = (self.dim * self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = (query @ key.transpose((- 2), (- 1)))
        qk = (qk / math.sqrt(self.dim))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, self.dropout, True)
        output = (attn_weight @ value)
        output = output.view((- 1), self.seq_len, self.head_dim)
        return output




func = Model().to('cuda')



query = torch.randn(1, 8, 64, 16)



key = torch.randn(1, 8, 64, 16)



value = torch.randn(1, 8, 64, 16)



attn_mask = torch.randn(1, 1, 64, 64)


test_inputs = [query, key, value, attn_mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2uhwe_dd/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp2uhwe_dd', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp2uhwe_dd/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''