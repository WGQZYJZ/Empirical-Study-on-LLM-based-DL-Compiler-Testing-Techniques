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
        self.avgpool2d = torch.nn.AvgPool2d(kernel_size=228)

    def forward(self, x3, x2):
        x3 = self.avgpool2d(x3)
        v1 = (x2 + x3)
        return v1




func = Model().to('cuda')



x3 = torch.randn(1, 3, 9, 7)



x2 = torch.randn(1, 2, 15, 13)


test_inputs = [x3, x2]
