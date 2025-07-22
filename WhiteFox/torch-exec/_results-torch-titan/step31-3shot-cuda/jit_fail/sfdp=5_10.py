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
        self.seq_len = 1
        self.dim = (6144 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = qk.transpose((- 1), (- 2)).transpose((- 3), (- 4))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        del qk
        attn_weight = torch.dropout(attn_weight, 2.3897206599917975e-06, True)
        attn_weight = attn_weight.transpose((- 1), (- 2)).transpose((- 2), (- 3))
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 6144, 1, 64)



key = torch.randn(1, 6144, 1, 64)



value = torch.randn(1, 6144, 1, 64)



attn_mask = torch.randn(1, 1, 1, 1)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:


jit:
backend='inductor' raised:
OutOfMemoryError: CUDA out of memory. Tried to allocate 9.00 GiB. GPU 0 has a total capacty of 23.69 GiB of which 4.96 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 18.46 GiB memory in use. Of the allocated memory 18.16 GiB is allocated by PyTorch, and 4.85 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''