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
        self.linear1 = torch.nn.Linear(3, 3)
        self.linear2 = torch.nn.Linear(3, 3)

    def forward(self, x):
        v1 = torch.nn.functional.hardtanh((x / self.linear1.weight))
        v2 = torch.nn.functional.linear(v1, self.linear2.weight, self.linear2.bias)
        x1 = torch.nn.functional.hardtanh((v1 / v2))
        v3 = torch.ops.aten.max(x1, dim=1, keepdim=True)
        v4 = torch.ops.aten.sinh(v3)
        v5 = torch.nn.functional.softmax((x1 / v4), dim=8)
        v6 = torch.nn.functional.hardtanh((x1 / v5))
        v7 = torch.ops.aten.cos(v6)
        v8 = torch.nn.functional.tanh((x1 / v7))
        v9 = (v8 + v8)
        v10 = (v9 + v7)
        v11 = (v10 - v5)
        v12 = v10.permute(0, 2, 1)
        v13 = torch.ops.aten.max(v11, dim=2, keepdim=True)
        v14 = torch.nn.functional.tanh((v13 * v12))
        v14 = v11.permute(0, 2, 1)
        return torch.nn.functional.sigmoid((v8 * v11))




func = Model().to('cuda')



x = torch.randn(2, 3, 4, 1, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Overloaded torch operator invoked from Python failed to many any schema:
aten::sinh() Expected a value of type 'Tensor' for argument 'self' but instead found type 'tuple'.
Position: 0
Value: (tensor([[[[[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-0.6888,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -0.9820],
           [ 1.0000,  1.0000,  1.0000]]]],



        [[[[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[ 0.6466,  1.0000,  1.0000],
           [ 1.0000, -0.9458,  0.8853],
           [ 0.2496,  1.0000,  1.0000]],

          [[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -1.0000],
           [ 0.8773,  1.0000,  1.0000]],

          [[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]]]]], device='cuda:0'), tensor([[[[[1, 0, 1],
           [1, 0, 0],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[2, 0, 0],
           [0, 0, 2],
           [2, 1, 0]]]],



        [[[[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]],

          [[2, 0, 1],
           [1, 1, 2],
           [2, 2, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [1, 1, 0]],

          [[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]]]]], device='cuda:0'))
Declaration: aten::sinh(Tensor self) -> Tensor
Cast error details: Unable to cast (tensor([[[[[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-0.6888,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -0.9820],
           [ 1.0000,  1.0000,  1.0000]]]],



        [[[[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[ 0.6466,  1.0000,  1.0000],
           [ 1.0000, -0.9458,  0.8853],
           [ 0.2496,  1.0000,  1.0000]],

          [[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -1.0000],
           [ 0.8773,  1.0000,  1.0000]],

          [[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]]]]], device='cuda:0'), tensor([[[[[1, 0, 1],
           [1, 0, 0],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[2, 0, 0],
           [0, 0, 2],
           [2, 1, 0]]]],



        [[[[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]],

          [[2, 0, 1],
           [1, 1, 2],
           [2, 2, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [1, 1, 0]],

          [[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]]]]], device='cuda:0')) to Tensor

aten::sinh() Expected a value of type 'Tensor' for argument 'self' but instead found type 'tuple'.
Position: 0
Value: (tensor([[[[[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-0.6888,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -0.9820],
           [ 1.0000,  1.0000,  1.0000]]]],



        [[[[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[ 0.6466,  1.0000,  1.0000],
           [ 1.0000, -0.9458,  0.8853],
           [ 0.2496,  1.0000,  1.0000]],

          [[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -1.0000],
           [ 0.8773,  1.0000,  1.0000]],

          [[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]]]]], device='cuda:0'), tensor([[[[[1, 0, 1],
           [1, 0, 0],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[2, 0, 0],
           [0, 0, 2],
           [2, 1, 0]]]],



        [[[[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]],

          [[2, 0, 1],
           [1, 1, 2],
           [2, 2, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [1, 1, 0]],

          [[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]]]]], device='cuda:0'))
Declaration: aten::sinh.out(Tensor self, *, Tensor(a!) out) -> Tensor(a!)
Cast error details: Unable to cast (tensor([[[[[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-0.6888,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -0.9820],
           [ 1.0000,  1.0000,  1.0000]]]],



        [[[[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[ 0.6466,  1.0000,  1.0000],
           [ 1.0000, -0.9458,  0.8853],
           [ 0.2496,  1.0000,  1.0000]],

          [[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -1.0000],
           [ 0.8773,  1.0000,  1.0000]],

          [[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]]]]], device='cuda:0'), tensor([[[[[1, 0, 1],
           [1, 0, 0],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[2, 0, 0],
           [0, 0, 2],
           [2, 1, 0]]]],



        [[[[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]],

          [[2, 0, 1],
           [1, 1, 2],
           [2, 2, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [1, 1, 0]],

          [[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]]]]], device='cuda:0')) to Tensor

aten::sinh() Expected a value of type 'int' for argument 'a' but instead found type 'tuple'.
Position: 0
Value: (tensor([[[[[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-0.6888,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -0.9820],
           [ 1.0000,  1.0000,  1.0000]]]],



        [[[[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[ 0.6466,  1.0000,  1.0000],
           [ 1.0000, -0.9458,  0.8853],
           [ 0.2496,  1.0000,  1.0000]],

          [[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -1.0000],
           [ 0.8773,  1.0000,  1.0000]],

          [[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]]]]], device='cuda:0'), tensor([[[[[1, 0, 1],
           [1, 0, 0],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[2, 0, 0],
           [0, 0, 2],
           [2, 1, 0]]]],



        [[[[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]],

          [[2, 0, 1],
           [1, 1, 2],
           [2, 2, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [1, 1, 0]],

          [[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]]]]], device='cuda:0'))
Declaration: aten::sinh.int(int a) -> float
Cast error details: Unable to cast Python instance of type <class 'tuple'> to C++ type '?' (#define PYBIND11_DETAILED_ERROR_MESSAGES or compile in debug mode for details)

aten::sinh() Expected a value of type 'float' for argument 'a' but instead found type 'tuple'.
Position: 0
Value: (tensor([[[[[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-0.6888,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -0.9820],
           [ 1.0000,  1.0000,  1.0000]]]],



        [[[[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[ 0.6466,  1.0000,  1.0000],
           [ 1.0000, -0.9458,  0.8853],
           [ 0.2496,  1.0000,  1.0000]],

          [[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -1.0000],
           [ 0.8773,  1.0000,  1.0000]],

          [[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]]]]], device='cuda:0'), tensor([[[[[1, 0, 1],
           [1, 0, 0],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[2, 0, 0],
           [0, 0, 2],
           [2, 1, 0]]]],



        [[[[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]],

          [[2, 0, 1],
           [1, 1, 2],
           [2, 2, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [1, 1, 0]],

          [[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]]]]], device='cuda:0'))
Declaration: aten::sinh.float(float a) -> float
Cast error details: Unable to cast Python instance of type <class 'tuple'> to C++ type '?' (#define PYBIND11_DETAILED_ERROR_MESSAGES or compile in debug mode for details)

aten::sinh() Expected a value of type 'complex' for argument 'a' but instead found type 'tuple'.
Position: 0
Value: (tensor([[[[[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-0.6888,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -0.9820],
           [ 1.0000,  1.0000,  1.0000]]]],



        [[[[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[ 0.6466,  1.0000,  1.0000],
           [ 1.0000, -0.9458,  0.8853],
           [ 0.2496,  1.0000,  1.0000]],

          [[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -1.0000],
           [ 0.8773,  1.0000,  1.0000]],

          [[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]]]]], device='cuda:0'), tensor([[[[[1, 0, 1],
           [1, 0, 0],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[2, 0, 0],
           [0, 0, 2],
           [2, 1, 0]]]],



        [[[[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]],

          [[2, 0, 1],
           [1, 1, 2],
           [2, 2, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [1, 1, 0]],

          [[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]]]]], device='cuda:0'))
Declaration: aten::sinh.complex(complex a) -> complex
Cast error details: Unable to cast Python instance of type <class 'tuple'> to C++ type '?' (#define PYBIND11_DETAILED_ERROR_MESSAGES or compile in debug mode for details)

aten::sinh() Expected a value of type 'number' for argument 'a' but instead found type 'tuple'.
Position: 0
Value: (tensor([[[[[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-0.6888,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -0.9820],
           [ 1.0000,  1.0000,  1.0000]]]],



        [[[[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[ 0.6466,  1.0000,  1.0000],
           [ 1.0000, -0.9458,  0.8853],
           [ 0.2496,  1.0000,  1.0000]],

          [[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -1.0000],
           [ 0.8773,  1.0000,  1.0000]],

          [[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]]]]], device='cuda:0'), tensor([[[[[1, 0, 1],
           [1, 0, 0],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[2, 0, 0],
           [0, 0, 2],
           [2, 1, 0]]]],



        [[[[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]],

          [[2, 0, 1],
           [1, 1, 2],
           [2, 2, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [1, 1, 0]],

          [[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]]]]], device='cuda:0'))
Declaration: aten::sinh.Scalar(Scalar a) -> Scalar
Cast error details: Cannot cast (tensor([[[[[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-1.0000,  1.0000, -1.0000],
           [-1.0000, -0.8460, -1.0000],
           [ 1.0000,  1.0000,  0.9469]],

          [[-0.6888,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -0.9820],
           [ 1.0000,  1.0000,  1.0000]]]],



        [[[[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]],

          [[ 0.6466,  1.0000,  1.0000],
           [ 1.0000, -0.9458,  0.8853],
           [ 0.2496,  1.0000,  1.0000]],

          [[-0.7003,  1.0000,  1.0000],
           [ 1.0000, -0.9458, -1.0000],
           [ 0.8773,  1.0000,  1.0000]],

          [[ 1.0000,  1.0000,  1.0000],
           [ 1.0000, -0.8460,  1.0000],
           [ 1.0000,  1.0000,  1.0000]]]]], device='cuda:0'), tensor([[[[[1, 0, 1],
           [1, 0, 0],
           [0, 0, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],

          [[2, 0, 0],
           [0, 0, 2],
           [2, 1, 0]]]],



        [[[[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]],

          [[2, 0, 1],
           [1, 1, 2],
           [2, 2, 1]],

          [[0, 0, 0],
           [0, 0, 0],
           [1, 1, 0]],

          [[1, 0, 2],
           [2, 0, 1],
           [0, 0, 2]]]]], device='cuda:0')) to number



jit:
Failed running call_function aten.sinh(*((FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64)),), **{}):
Overloaded torch operator invoked from Python failed to many any schema:
aten::sinh() Expected a value of type 'Tensor' for argument 'self' but instead found type 'tuple'.
Position: 0
Value: (FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64))
Declaration: aten::sinh(Tensor self) -> Tensor
Cast error details: Unable to cast (FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64)) to Tensor

aten::sinh() Expected a value of type 'Tensor' for argument 'self' but instead found type 'tuple'.
Position: 0
Value: (FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64))
Declaration: aten::sinh.out(Tensor self, *, Tensor(a!) out) -> Tensor(a!)
Cast error details: Unable to cast (FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64)) to Tensor

aten::sinh() Expected a value of type 'int' for argument 'a' but instead found type 'tuple'.
Position: 0
Value: (FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64))
Declaration: aten::sinh.int(int a) -> float
Cast error details: Unable to cast Python instance of type <class 'tuple'> to C++ type '?' (#define PYBIND11_DETAILED_ERROR_MESSAGES or compile in debug mode for details)

aten::sinh() Expected a value of type 'float' for argument 'a' but instead found type 'tuple'.
Position: 0
Value: (FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64))
Declaration: aten::sinh.float(float a) -> float
Cast error details: Unable to cast Python instance of type <class 'tuple'> to C++ type '?' (#define PYBIND11_DETAILED_ERROR_MESSAGES or compile in debug mode for details)

aten::sinh() Expected a value of type 'complex' for argument 'a' but instead found type 'tuple'.
Position: 0
Value: (FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64))
Declaration: aten::sinh.complex(complex a) -> complex
Cast error details: Unable to cast Python instance of type <class 'tuple'> to C++ type '?' (#define PYBIND11_DETAILED_ERROR_MESSAGES or compile in debug mode for details)

aten::sinh() Expected a value of type 'number' for argument 'a' but instead found type 'tuple'.
Position: 0
Value: (FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64))
Declaration: aten::sinh.Scalar(Scalar a) -> Scalar
Cast error details: Cannot cast (FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3)), FakeTensor(..., device='cuda:0', size=(2, 1, 4, 3, 3), dtype=torch.int64)) to number



from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''