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
        self.heads = 8
        self.seq_len = 484
        self.dim = (96 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, 0.003, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



dim = 16


seq_len = 520


heads = 8


batch_size = 1


query = torch.randn(batch_size, heads, seq_len, dim)



dim = 16


seq_len = 520


heads = 8


batch_size = 1


key = torch.randn(batch_size, heads, seq_len, dim)



dim = 16


seq_len = 520


heads = 8


batch_size = 1


value = torch.randn(batch_size, heads, seq_len, dim)



seq_len = 520


seq_len = 520


batch_size = 1


attn_mask = torch.randn(batch_size, 1, seq_len, seq_len)


test_inputs = [query, key, value, attn_mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9wlvbvy0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9wlvbvy0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9wlvbvy0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''