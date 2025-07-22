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

    def forward(self, x1):
        b = {}
        a = {}
        b['dtype'] = torch.int64
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.int32
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.int64
        a['dtype_from'] = torch.int32
        b['dtype_to'] = torch.int64
        b['dtype_from'] = torch.int32
        t1 = torch.full([800000000, 1], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3




func = Model().to('cuda')



x1 = torch.randn(800000000, 1, device='cuda:0')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 5.96 GiB. GPU 0 has a total capacty of 23.69 GiB of which 5.25 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 18.17 GiB memory in use. Of the allocated memory 17.88 GiB is allocated by PyTorch, and 0 bytes is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
OutOfMemoryError: CUDA out of memory. Tried to allocate 5.96 GiB. GPU 0 has a total capacty of 23.69 GiB of which 5.25 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 18.17 GiB memory in use. Of the allocated memory 17.88 GiB is allocated by PyTorch, and 0 bytes is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

While executing %cumsum : [num_users=1] = call_function[target=torch.ops.aten.cumsum.default](args = (%convert_element_type, 1), kwargs = {})
Original traceback:
  File "<string>", line 35, in forward



You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''