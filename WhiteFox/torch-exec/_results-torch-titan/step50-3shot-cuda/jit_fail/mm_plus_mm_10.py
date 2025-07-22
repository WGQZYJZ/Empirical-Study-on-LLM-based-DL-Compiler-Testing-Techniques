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

    def forward(self, in1, in2, in3, in4):
        t1 = torch.nn.functional.matmul(in1, in2)
        t2 = torch.nn.functional.matmul(in3, in4)
        return (t1 * t2)




func = Model().to('cuda')



in1 = torch.randn(16, 8)



in2 = torch.randn(8, 16)



in3 = torch.randn(16, 8)



in4 = torch.randn(8, 16)


test_inputs = [in1, in2, in3, in4]

# JIT_FAIL
'''
direct:
module 'torch.nn.functional' has no attribute 'matmul'

jit:
module 'torch.nn.functional' has no attribute 'matmul'

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''