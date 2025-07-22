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
        b['dtype'] = torch.complex128
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.complex32
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.complex32
        a['dtype_from'] = torch.complex128
        b['dtype_to'] = torch.complex128
        b['dtype_from'] = torch.complex32
        t1 = torch.full([8, 16], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3




func = Model().to('cuda')



x1 = torch.randn(8, 16, 2, device='cuda:0')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
"cumsum_cuda" not implemented for 'ComplexHalf'

jit:
backend='inductor' raised:
RuntimeError: "cumsum_cuda" not implemented for 'ComplexHalf'

While executing %cumsum : [num_users=1] = call_function[target=torch.ops.aten.cumsum.default](args = (%convert_element_type, 1), kwargs = {})
Original traceback:
  File "<string>", line 35, in forward



You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''