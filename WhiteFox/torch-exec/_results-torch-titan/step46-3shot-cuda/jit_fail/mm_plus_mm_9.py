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

    def forward(self, input1, input2, input3, input4, input5, input6):
        t1 = torch.mm(input1, input1)
        t2 = torch.mm(input2, input2)
        t3 = torch.mm(input3, input3)
        t4 = torch.mm(input4, input4)
        t5 = torch.mm(input5, input5)
        t6 = torch.mm(input6, input6)
        return (((((t1 + t2) + t3) + t4) + t5) + t6)




func = Model().to('cuda')



input1 = torch.randn(10, 10)



input2 = torch.randn(10, 10)



input3 = torch.randn(10, 10)

input4 = 1
input5 = 1
input6 = 1

test_inputs = [input1, input2, input3, input4, input5, input6]

# JIT_FAIL
'''
direct:
mm(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method mm of type object at 0x7faf32c699e0>(*(1, 1), **{}):
mm(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''