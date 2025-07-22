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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.Conv2d(32, 32, 4, 1, 5))
        self.split = torch.nn.Sequential()
        self.concat = torch.nn.Sequential()

    def forward(self, v1):
        split_tensors = []
        for i in range(3):
            split_tensors.append(torch.split(v1, [1, 1, 1], dim=1))
        for i in range(len(split_tensors)):
            for j in range(3):
                if (split_tensors[i][j].shape[1] > 1):
                    split_tensors[i][j] = torch.split(split_tensors[i][j], [1, 1, 1], dim=1)
        concatenated_tensor = []
        for i in range(3):
            concatenated_tensor.append(torch.cat([(split_tensors[i][j][0] for j in range(3))], dim=1))
        for i in range(len(split_tensors)):
            for j in range(3):
                if (split_tensors[i][j].shape[1] > 1):
                    concatenated_tensor[i] = torch.cat([concatenated_tensor[i], torch.split(concatenated_tensor[i], [1, 1, 1], dim=1)], dim=1)
        return (torch.cat(concatenated_tensor, dim=1), split_tensors)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got generator

jit:
expected Tensor as element 0 in argument 0, but got generator
'''