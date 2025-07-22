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
        self.key = torch.nn.Parameter(torch.randn(953, 36, 2644, 1))

    def forward(self, x1):
        q = x1
        k = x1
        v = x1
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(v)
        return output




func = Model().to('cuda')



x1 = torch.randn(1, 1053, 1355, 25)


test_inputs = [x1]

# JIT_FAIL
'''
direct:


jit:
backend='inductor' raised:
OutOfMemoryError: CUDA out of memory. Tried to allocate 7.22 GiB. GPU 0 has a total capacty of 23.69 GiB of which 7.09 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 16.33 GiB memory in use. Of the allocated memory 15.65 GiB is allocated by PyTorch, and 397.31 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''