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
        b['device'] = torch.device('cpu:0')
        a['dtype'] = torch.float16
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.float64
        a['dtype_from'] = torch.float32
        b['dtype_to'] = torch.double
        b['dtype_from'] = torch.float64
        t1 = torch.full([16, 256], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3




func = Model().to('cuda')



x1 = torch.randn(16, 256, device='cuda:0')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
"cumsum_out_cpu" not implemented for 'Half'

jit:
backend='inductor' raised:
RuntimeError: "cumsum_out_cpu" not implemented for 'Half'

While executing %cumsum : [num_users=1] = call_function[target=torch.ops.aten.cumsum.default](args = (%convert_element_type, 1), kwargs = {})
Original traceback:
  File "<string>", line 35, in forward



You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''