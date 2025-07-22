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
        b['dtype'] = torch.float32
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.float16
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.float32
        a['dtype_from'] = torch.float16
        b['dtype_to'] = torch.float32
        b['dtype_from'] = torch.float16
        t1 = torch.randn([1048576, 2048], device=b['device'])
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 0)
        return t3




func = Model().to('cuda')



x1 = torch.randn(1048576, 2048, device='cuda:0')


test_inputs = [x1]

# CRASH
'''
crash:
CUDA out of memory. Tried to allocate 8.00 GiB. GPU 0 has a total capacty of 23.69 GiB of which 7.11 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 16.31 GiB memory in use. Of the allocated memory 16.01 GiB is allocated by PyTorch, and 7.47 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF
'''