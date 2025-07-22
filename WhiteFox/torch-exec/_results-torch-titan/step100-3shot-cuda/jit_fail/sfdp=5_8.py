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
        self.heads = 31
        self.seq_len = 4260
        self.dim = (1771 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, 0.6, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 31, 4260, 1771)



key = torch.randn(1, 31, 4260, 1771)



value = torch.randn(1, 31, 4260, 1771)



attn_mask = torch.randn(1, 1, 4260, 4260)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:


jit:
backend='inductor' raised:
OutOfMemoryError: CUDA out of memory. Tried to allocate 894.00 MiB. GPU 0 has a total capacty of 23.69 GiB of which 381.00 MiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 23.05 GiB memory in use. Of the allocated memory 17.75 GiB is allocated by PyTorch, and 5.00 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''