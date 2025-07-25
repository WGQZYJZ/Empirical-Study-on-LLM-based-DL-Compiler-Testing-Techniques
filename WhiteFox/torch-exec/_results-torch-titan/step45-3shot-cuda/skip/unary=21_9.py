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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, (17, 1), stride=(1, 1))
        self.conv2 = torch.nn.Conv2d(7, 13, (6, 1), stride=(48, 1), padding=(1, 1), groups=246)
        self.conv3 = torch.nn.Conv2d(259, 128, (6, 1), stride=(48, 1), bias=False)
        self.relu = torch.nn.ReLU()
        self.tanh = torch.nn.Tanh()

    def forward(self, x0):
        t0 = self.conv1(x0)
        t1 = self.conv2(t0)
        t2 = self.conv3(t1)
        t3 = self.relu(t2)
        return self.tanh(t3)




func = ModelTanh().to('cuda')



x0 = torch.randn(1, 3, 2, 2)


test_inputs = [x0]
