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

    def __init__(self, input_length, hidden_size, num_heads, num_layers):
        super().__init__()
        self.transformer = torch.nn.Transformer(d_model=hidden_size, nhead=num_heads, num_encoder_layers=num_layers, num_decoder_layers=num_layers)

    def forward(self, x1, x2):
        x3 = self.transformer(x1, x2)
        return x3




input_length = 96


hidden_size = 8


num_heads = 2


num_layers = 2

func = Model(input_length, hidden_size, num_heads, num_layers).to('cuda')



x1 = torch.rand(1, 96, 64).to(device=0)



x2 = torch.rand(1, 96, 64).to(device=0)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
the feature number of src and tgt must be equal to d_model

jit:
Failed running call_module L__self___transformer(*(FakeTensor(..., device='cuda:0', size=(1, 96, 64)), FakeTensor(..., device='cuda:0', size=(1, 96, 64))), **{}):
the feature number of src and tgt must be equal to d_model

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''