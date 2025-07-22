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
        self.dropout = 0.7854209996613659
        self.heads = 64
        self.seq_len = 16384
        self.dim = (64 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, self.dropout, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 128, 16384, 64)



key = torch.randn(1, 128, 16384, 64)



value = torch.randn(1, 128, 16384, 64)



attn_mask = torch.randn(1, 1, 16384, 16384)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 128.00 GiB. GPU 0 has a total capacty of 23.69 GiB of which 13.96 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 9.46 GiB memory in use. Of the allocated memory 5.66 GiB is allocated by PyTorch, and 3.50 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7fopyv4v/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp7fopyv4v', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp7fopyv4v/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''