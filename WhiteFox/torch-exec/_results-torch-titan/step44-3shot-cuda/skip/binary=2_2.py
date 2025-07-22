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
        self.depthwise_conv = torch.nn.Conv2d(1, 16, (3, 3), stride=(2, 2), padding=(2, 2), groups=16, bias=False)
        self.pointwise_conv = torch.nn.Conv2d(16, 16, (3, 3), stride=(1, 1), padding=(1, 1), bias=False)

    def forward(self, x):
        v1 = self.depthwise_conv(x)
        v2 = self.pointwise_conv(v1)
        v3 = (v2 - 2.09)
        return v3




func = Model().to('cuda')



x = torch.randn(1, 1, 48, 48)


test_inputs = [x]
