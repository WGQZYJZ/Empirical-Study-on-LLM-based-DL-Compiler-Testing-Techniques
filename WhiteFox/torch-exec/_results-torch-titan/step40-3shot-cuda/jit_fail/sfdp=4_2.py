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

    def forward(self, input, input2, input3, mask):
        input2 = input2.permute(1, 0, 2, 3)
        qk = ((input @ input2) / math.sqrt(input2.size((- 1))))
        qk_mask = mask.view(qk.size())
        qk = qk.masked_fill((qk_mask != 0), qk_mask[(qk_mask != 0)])
        q3 = qk.permute(1, 0, 2, 3)
        attn_weight = torch.softmax(q3, dim=(- 1))
        output = (attn_weight @ input3)
        return (q3, output)




func = Model().to('cuda')



Q = torch.randn(1, 64, 56, 56)



K = torch.randn(1, 64, 56, 56)



V = torch.randn(1, 64, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))


test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
shape '[64, 64, 56, 56]' is invalid for input of size 3136

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 56, 56), dtype=torch.bool), (64, 64, 56, 56)), **{}):
shape '[64, 64, 56, 56]' is invalid for input of size 3136

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''