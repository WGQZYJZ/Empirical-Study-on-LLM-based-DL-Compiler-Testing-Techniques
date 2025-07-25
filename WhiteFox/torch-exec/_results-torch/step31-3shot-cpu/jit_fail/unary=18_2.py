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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=512, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))
        self.bn1 = torch.nn.BatchNorm2d(512)
        self.conv3 = torch.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))
        self.bn2 = torch.nn.BatchNorm2d(256)
        self.max_pooling1 = torch.nn.MaxPool2d(kernel_size=(2, 2), padding=(0, 1), stride=(2, 2), dilation=(1, 1))
        self.conv4 = torch.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))
        self.conv5 = torch.nn.Conv2d(in_channels=128, out_channels=192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.bn3 = torch.nn.BatchNorm2d(192)
        self.conv6 = torch.nn.Conv2d(in_channels=192, out_channels=128, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))
        self.conv7 = torch.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.bn4 = torch.nn.BatchNorm2d(128)
        self.max_pooling2 = torch.nn.MaxPool2d(kernel_size=(2, 2), padding=(0, 1), stride=(2, 2), dilation=(1, 1))
        self.flatten = torch.nn.Flatten()
        self.linear1 = torch.nn.Linear(in_features=128, out_features=64, bias=True)
        self.linear2 = torch.nn.Linear(in_features=64, out_features=1, bias=True)

    def forward(self, input_image):
        x1 = self.conv1(input_image)
        x2 = gum_sigmoid_function(x1)
        x3 = self.conv2(x2)
        x4 = self.bn1(x3)
        x5 = torch.sigmoid(x4)
        x6 = self.conv3(x5)
        x7 = self.bn2(x6)
        x8 = gum_sigmoid_function(x7)
        x9 = self.max_pooling1(x8)
        x10 = self.conv4(x9)
        x11 = self.conv5(x10)
        x12 = self.bn3(x11)
        x13 = gum_sigmoid_function(x12)
        x14 = self.conv6(x13)
        x15 = self.conv7(x14)
        x16 = self.bn4(x15)
        x17 = gum_sigmoid_function(x16)
        x18 = self.max_pooling2(x17)
        x19 = self.flatten(x18)
        x20 = self.linear1(x19)
        x21 = self.linear2(x20)
        x22 = torch.sigmoid(x21)
        return x22



func = Model().to('cpu')


input_image = torch.randn(1, 3, 16, 16)

test_inputs = [input_image]

# JIT_FAIL
'''
direct:
name 'gum_sigmoid_function' is not defined

jit:
NameError: name 'gum_sigmoid_function' is not defined

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''