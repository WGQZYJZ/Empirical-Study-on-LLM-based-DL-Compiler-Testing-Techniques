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

    def __init__(self, attention_head_size=8):
        super().__init__()
        self.attention_head_size = attention_head_size
        self.q = torch.nn.Linear(768, attention_head_size)
        self.k = torch.nn.Linear(768, attention_head_size)
        self.v = torch.nn.Linear(768, attention_head_size)
        self.o = torch.nn.Linear(attention_head_size, 768)

    def forward(self, query, key, value, attn_mask):
        q = self.q(query)
        k = self.k(key)
        v = self.v(value)
        qk = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(k.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v)
        output = self.o(output)
        return output



func = Model().to('cuda')



query = torch.randn(1, 64, 768)



key = torch.randn(1, 64, 768)



value = torch.randn(1, 64, 768)



attn_mask = torch.ones(1, 64, 64)


test_inputs = [query, key, value, attn_mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpainzgsia/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpainzgsia', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpainzgsia/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''