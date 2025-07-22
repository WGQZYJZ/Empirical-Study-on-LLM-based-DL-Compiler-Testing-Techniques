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
        self.heads = 93
        self.seq_len = 6144
        self.dim = (155 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, 0.7, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 93, 6144, 155)



key = torch.randn(1, 93, 6144, 155)



value = torch.randn(1, 93, 6144, 155)



attn_mask = torch.randn(1, 1, 6144, 6144)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 13.08 GiB. GPU 0 has a total capacty of 23.69 GiB of which 7.80 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 15.62 GiB memory in use. Of the allocated memory 15.35 GiB is allocated by PyTorch, and 11.88 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
OutOfMemoryError: CUDA out of memory. Tried to allocate 13.08 GiB. GPU 0 has a total capacty of 23.69 GiB of which 7.43 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 15.99 GiB memory in use. Of the allocated memory 15.68 GiB is allocated by PyTorch, and 13.87 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''