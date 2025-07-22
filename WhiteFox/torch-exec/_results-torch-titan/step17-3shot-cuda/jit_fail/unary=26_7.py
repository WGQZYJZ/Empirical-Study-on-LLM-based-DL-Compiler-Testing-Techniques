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

    def __init__(self, input_size, num_channels, maxpool_stride, num_classes):
        super().__init__()
        self.conv_t1 = torch.nn.ConvTranspose3d(in_channels=input_size, out_channels=num_channels, kernel_size=(8, 9, 4), stride=(2, 2, 2))
        self.conv_t2 = torch.nn.ConvTranspose3d(in_channels=num_channels, out_channels=num_channels, kernel_size=(8, 10, 6), stride=(1, 2, 2))
        self.avgpool = torch.nn.AvgPool3d(kernel_size=maxpool_stride, stride=maxpool_stride)
        self.flatten = torch.nn.Flatten()
        self.fc = torch.nn.Linear(num_channels, num_classes)

    def forward(self, x):
        x1 = self.conv_t1(x)
        x2 = torch.relu(x1)
        x3 = self.conv_t2(x2)
        x4 = torch.relu(x3)
        x5 = self.avgpool(x4)
        x6 = self.flatten(x5)
        x7 = self.fc(x6)
        return x7




input_size = 512


num_channels = 56


maxpool_stride = 2


num_classes = 5

func = Model(input_size, num_channels, maxpool_stride, num_classes).to('cuda')



input_size = 512


input_data = torch.randn(16, input_size, 32, 48, 64)



num_classes = 5


output_data = torch.randn(16, num_classes)


test_inputs = [input_data, output_data]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''