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

    def forward(self, x1, x2, x3, x4, x7):
        x1_2 = x1[:, :, :, :105]
        x1_3 = x1[:, :, :, 25:130]
        x1_4 = x1[:, :, :, 105:210]
        x1_5 = x1[:, :, :, 185:290]
        x1_6 = x1[:, :, :, 290:395]
        x2_2 = x2[:, :, 8:12]
        x3_2 = x3[:, :, 5:9]
        x4_2 = x4[:, :, 83:87]
        x7_2 = x7[:, :, 87:91]
        t1 = torch.cat([x1_2, x1_3, x1_4, x1_5, x1_6], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3_1 = t2[:, 87:184]
        t3_2 = t2[:, 351:448]
        t3_3 = t2[:, 615:712]
        t4_1 = torch.cat([t1, t3_1], dim=1)
        t4_2 = torch.cat([t1, t3_2], dim=1)
        t4_3 = torch.cat([t1, t3_3], dim=1)
        t4_4 = torch.cat([t4_1, x2_2], dim=1)
        t4_5 = torch.cat([t4_2, x3_2], dim=1)
        t4_6 = torch.cat([t4_3, x4_2], dim=1)
        t4_7 = torch.cat([t4_6, x7_2], dim=1)
        v0 = t4_4
        v1 = t4_5
        v2 = t4_7
        return (v0, v1, v2)



func = Model().to('cuda')



x1 = torch.randn(1, 775, 775, 3)



x2 = torch.randn(1, 3, 4, 9)



x3 = torch.randn(1, 3, 4, 9)



x4 = torch.randn(1, 3, 8, 8)



x7 = torch.randn(1, 3, 8, 8)


test_inputs = [x1, x2, x3, x4, x7]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 3 but got size 0 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x74115b0699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 775, 775, 3)), FakeTensor(..., device='cuda:0', size=(1, 775, 775, 0)), FakeTensor(..., device='cuda:0', size=(1, 775, 775, 0)), FakeTensor(..., device='cuda:0', size=(1, 775, 775, 0)), FakeTensor(..., device='cuda:0', size=(1, 775, 775, 0))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 3 but got 0 for tensor number 1 in the list

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''