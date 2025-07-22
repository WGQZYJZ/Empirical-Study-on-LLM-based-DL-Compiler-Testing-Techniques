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
        self.conv1 = torch.nn.Conv2d(1, 1, 3, stride=1, padding=0)

    def forward(self, x1):
        b = {}
        a = {}
        b['dtype'] = torch.float32
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.float32
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.float16
        a['dtype_from'] = torch.float32
        b['dtype_to'] = torch.float32
        b['dtype_from'] = torch.float16
        t1 = torch.full([256, 3, 2560, 2048], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = t2.sum(dim=2)
        t4 = torch.cumsum(t3, 1)
        t5 = t4.type(torch.float16)
        t6 = t5.div(2560)
        return t6




func = Model().to('cuda')



x1 = torch.randn(256, 1, 2560, 2048, device='cuda:0')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 15.00 GiB. GPU 0 has a total capacty of 23.69 GiB of which 8.01 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 15.42 GiB memory in use. Of the allocated memory 15.05 GiB is allocated by PyTorch, and 76.56 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
OutOfMemoryError: CUDA out of memory. Tried to allocate 15.00 GiB. GPU 0 has a total capacty of 23.69 GiB of which 8.01 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 15.42 GiB memory in use. Of the allocated memory 15.03 GiB is allocated by PyTorch, and 96.39 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

While executing %full : [num_users=1] = call_function[target=torch.ops.aten.full.default](args = ([256, 3, 2560, 2048], 1), kwargs = {dtype: torch.float32, layout: torch.strided, device: cuda:0, pin_memory: False})
Original traceback:
  File "<string>", line 34, in forward



You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''