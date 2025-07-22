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



class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.conv_t = Conv2dT(32, 3, 2, stride=2, padding=1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.conv_t(x)
        x = self.sigmoid(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 32, 32, 32)


test_inputs = [x]
