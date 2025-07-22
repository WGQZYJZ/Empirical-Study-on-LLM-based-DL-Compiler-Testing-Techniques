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

    def forward(self, x, y, z, inv_scale_factor, dropout_p):
        return torch.nn.functional.multi_head_attention_forward(query=x, key=y, value=z, in_proj_weight=None, in_proj_bias=None, bias_k=None, bias_v=None, add_zero_attn=False, dropout_p=0.2, out_proj_weight=None, out_proj_bias=None, use_separate_proj_weight=False, training=False, dropout_state=None, find_unused_parameters=True)



func = Model().to('cuda')



x = torch.randn(2, 3, 4, 20)



y = torch.randn(2, 5, 6, 16)



z = torch.randn(2, 5, 6, 16)

inv_scale_factor = 1
dropout_p = 1

test_inputs = [x, y, z, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
multi_head_attention_forward() got an unexpected keyword argument 'dropout_state'

jit:
Failed running call_function <function multi_head_attention_forward at 0x7693200fe040>(*(), **{'query': FakeTensor(..., device='cuda:0', size=(2, 3, 4, 20)), 'key': FakeTensor(..., device='cuda:0', size=(2, 5, 6, 16)), 'value': FakeTensor(..., device='cuda:0', size=(2, 5, 6, 16)), 'in_proj_weight': None, 'in_proj_bias': None, 'bias_k': None, 'bias_v': None, 'add_zero_attn': False, 'dropout_p': 0.2, 'out_proj_weight': None, 'out_proj_bias': None, 'use_separate_proj_weight': False, 'training': False, 'dropout_state': None, 'find_unused_parameters': True}):
multi_head_attention_forward() got an unexpected keyword argument 'dropout_state'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''