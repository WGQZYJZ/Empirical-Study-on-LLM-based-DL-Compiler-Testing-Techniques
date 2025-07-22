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

    def forward(self, model_input, model_input_2, model_input_3, model_input_4):
        v1 = torch.mm(model_input, model_input)
        v2 = torch.mm(model_input_3, model_input_4)
        return (v1 * v2)




func = Model().to('cuda')



model_input = torch.randn(10, 10)



model_input_2 = torch.randn(33, 33)



model_input_3 = torch.randn(19, 19)



model_input_4 = torch.randn(87, 87)


test_inputs = [model_input, model_input_2, model_input_3, model_input_4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (19x19 and 87x87)

jit:
Failed running call_function <built-in method mm of type object at 0x777646e699e0>(*(FakeTensor(..., device='cuda:0', size=(19, 19)), FakeTensor(..., device='cuda:0', size=(87, 87))), **{}):
a and b must have same reduction dim, but got [19, 19] X [87, 87].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''