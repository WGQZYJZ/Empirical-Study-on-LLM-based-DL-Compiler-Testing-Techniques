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



class TestModule1(torch.nn.Module):

    def __init__(self, conv=torch.conv2d, weight=None):
        super(TestModule1, self).__init__()
        if (weight is None):
            self.conv = conv
        else:
            self.conv = conv(1, 1, kernel_size=(2, 2), groups=1, bias=True, padding=0, stride=1, dilation=1)
            with torch.no_grad():
                self.conv.weight.copy_(weight)

    def forward(self, x):
        x = self.conv(x)
        return x



func = TestModule1(conv=TestModule1.conv, weight=m).to('cuda')



x1 = torch.randn(1, 10, 16, 10)



m = torch.rand(1, 1, 2, 2)


test_inputs = [x1, m]
