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

    def forward(self, input1d, weight1d, weight1d_, input2d, weight2d, weight2d_, input3d, weight3d, weight3d_, bias1d, bias2d, bias3d, bias3d_):
        conv1d = torch.nn.functional.conv1d(input1d, weight1d, None, [2, 1], 0, 1)
        conv1d_ = torch.nn.functional.conv1d(input1d, weight1d_, bias1d, [2, 1], 0, 1)
        bn1d = torch.nn.functional.batch_norm(conv1d)
        bn1d_ = torch.nn.functional.batch_norm(conv1d_, weight1d_.shape[0])
        bn1d.weight.data = bn1d_.weight.data
        bn1d.bias.data = bn1d_.bias.data
        bn1d.running_mean = bn1d_.running_mean
        bn1d.running_var = bn1d_.running_var
        bn1d.momentum = bn1d_.momentum
        bn1d.eps = bn1d_.eps
        input2d = torch.nn.functional.relu(torch.nn.functional.batch_norm(torch.nn.functional.conv2d(input2d, weight2d, None, [2, 1, 2, 1], 0, 1)))
        input2d_ = torch.nn.functional.relu(torch.nn.functional.batch_norm(torch.nn.functional.conv2d(input2d, weight2d_, bias2d, [2, 1, 2, 1], 0, 1), weight2d_.shape[0]))
        weight2d.data = (torch.randn_like(weight2d) + weight2d_)
        weight2d.requires_grad_ = False
        weight2d.is_contiguous()
        input3d = torch.nn.functional.relu(torch.nn.functional.batch_norm(torch.nn.functional.conv3d(input3d, weight3d, None, [2, 1, 2, 1, 2, 1], 0, 1)))
        input3d_ = torch.nn.functional.batch_norm(torch.nn.functional.conv3d(input3d, weight3d_, bias3d, [2, 1, 2, 1, 2, 1], 0, 1), weight3d_.shape[1])
        weight3d.data = (torch.randn_like(weight3d) + weight3d_)
        weight3d.requires_grad_ = False
        weight3d.is_contiguous()
        conv3d = torch.nn.functional.conv3d(input3d, weight3d, None, [2, 1, 2, 1, 2, 1], 0, 1)
        conv3d_ = torch.nn.functional.conv3d(input3d, weight3d_, bias3d_, [2, 1, 2, 1, 2, 1], 0, 1)
        return (conv1d, bn1d, conv1d_, input2d, input2d_, weight2d, weight2d, weight2d_, conv3d, conv3d_, input3d, input3d_, weight3d, weight3d_, weight3d_)




func = Model().to('cuda')



input1d = torch.randn(2, 4, 1)



weight1d = torch.randn(4, 4, 2)



weight1d = torch.randn(4, 4, 2)


weight1d_ = torch.randn_like(weight1d)



input2d = torch.randn(1, 3, 10, 14)



weight2d = torch.randn(7, 3, 2, 3)



weight2d = torch.randn(7, 3, 2, 3)


weight2d_ = torch.randn_like(weight2d)



input3d = torch.randn(1, 3, 12, 14, 18)



weight3d = torch.randn(4, 3, 2, 3, 4)



weight3d = torch.randn(4, 3, 2, 3, 4)


weight3d_ = torch.randn_like(weight3d)



bias1d = torch.randn(4)



bias2d = torch.randn(7)



bias3d = torch.randn(4)



bias3d_ = torch.randn(4)


test_inputs = [input1d, weight1d, weight1d_, input2d, weight2d, weight2d_, input3d, weight3d, weight3d_, bias1d, bias2d, bias3d, bias3d_]

# JIT_FAIL
'''
direct:
expected stride to be a single integer value or a list of 1 values to match the convolution dimensions, but got stride=[2, 1]

jit:
Failed running call_function <function batch_norm at 0x76f6e4be3b80>(*(FakeTensor(..., device='cuda:0', size=(2, 4, 0)),), **{}):
batch_norm() missing 2 required positional arguments: 'running_mean' and 'running_var'

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''