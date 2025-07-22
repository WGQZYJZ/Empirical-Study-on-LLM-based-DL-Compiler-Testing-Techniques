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
        self.conv1 = torch.nn.Conv2d(1, 64, kernel_size=(1, 9), stride=(1, 4), padding=(0, 4), dilation=2, groups=2, bias=True)
        self.conv2 = torch.nn.Conv2d(1, 64, kernel_size=(1, 9), stride=(1, 4), padding=(0, 2), dilation=2, groups=2, bias=True)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(x1)
        v4 = torch.sigmoid(v3)
        return (v2, v4)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 224, 224)


test_inputs = [x1]
