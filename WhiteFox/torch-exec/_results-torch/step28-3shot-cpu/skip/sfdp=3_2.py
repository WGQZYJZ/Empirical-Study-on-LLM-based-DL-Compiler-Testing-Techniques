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

class ResidualAttentionBlock(torch.nn.Module):

    def __init__(self, d_feature, dropout=0.1):
        super().__init__()
        __________________________________
        pass

    def forward(self, x):
        __________________________________
        pass
        return x


d_feature = 64
func = ResidualAttentionBlock(d_feature, dropout).to('cpu')


x1 = torch.randn(1, 1024, 64)

x2 = torch.randn(1, 64, 128)

x3 = torch.randn(1, 128, 256)

test_inputs = [x1, x2, x3]
