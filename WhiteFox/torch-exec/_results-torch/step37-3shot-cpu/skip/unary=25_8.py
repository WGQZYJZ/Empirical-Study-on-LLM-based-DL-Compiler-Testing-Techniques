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

    def __init__(self, negative_slope):
        super(Model).__init__()
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = x1.shape[1]
        v2 = math.exp(negative_slope)
        v3 = torch.zeros(v1)
        v4 = torch.add(v2, 1)
        v5 = torch.multiply(v4, v3)
        v6 = v5[0:Negative_slope]
        v7 = v6[0:Negative_slope[0:Negative_slope]]
        v8 = torch.nn.functional.max_pool2d(x1, kernel_size=Kernel_Size, stride=Stride, padding=Padding, dilation=Dilation, ceil_mode=Ceil_Mode)
        v9 = v7.flatten(start_dim=Start_Dim, end_dim=-1)
        v10 = v8 + v9
        return v10


negative_slope = 1

func = Model(negative_slope).to('cpu')

x1 = 1

test_inputs = [x1]
