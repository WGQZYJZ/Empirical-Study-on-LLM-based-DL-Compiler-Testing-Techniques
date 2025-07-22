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
        self.conv = torch.nn.Conv2d(in_channels, 3, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.batchNorm = torch.nn.BatchNorm2d(num_features)
        self.dropout = nn.Dropout(p=0.1)
        self.leakyrelu = torch.nn.LeakyReLU()
        self.maxpool = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        x = self.conv(x)
        x = self.batchNorm(x)
        x = self.dropout(x)
        x = self.leakyrelu(x)
        x = self.maxpool(x)
        return x



func = Model().to('cpu')

input_shape = (1, 3, 32, 32)

input_shape = (1, 3, 32, 32)
x = torch.randn(*input_shape)

test_inputs = [x]
