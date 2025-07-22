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

    def forward(self, Q5, k, v, mask):
        qk = ((Q5 @ k.transpose((- 2), (- 1))) / math.sqrt(Q5.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v)
        output2 = self.layer1(output)
        output3 = (output2 + output)
        x = self.layer2(output3)
        output4 = self.layer3_b(x)
        output5 = (output4 + output3)
        output6 = self.layer3_a(output5)
        ouput7 = (output6 + output)
        attention_map = torch.softmax(qk.mean(0), 0)
        attention_map = (attention_map / torch.sum(attention_map, 0, keepdim=True))
        return output




func = Model().to('cuda')



Q = torch.randn(1, 64, 56, 56)



K = torch.randn(1, 64, 56, 56)



V = torch.randn(1, 64, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))


test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'layer1'

jit:
layer1

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''