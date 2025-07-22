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



class MultiHeadAttention(torch.nn.Module):

    def __init__(self, d_k):
        super().__init__()
        self.d_k = d_k

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(self.d_k))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ value)
        return output



d_k = 1
func = MultiHeadAttention(d_k).to('cuda')



query = torch.randn(2, 4, 9)



key = torch.randn(2, 10, 9)



value = torch.randn(2, 10, 9)



attn_mask = torch.randn(2, 1, 4, 10)


test_inputs = [query, key, value, attn_mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplzufoymh/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmplzufoymh', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmplzufoymh/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''