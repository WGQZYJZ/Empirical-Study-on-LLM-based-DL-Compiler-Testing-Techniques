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

    def __init__(self, min_value):
        super().__init__()
        self.conv0 = torch.nn.Conv2d(512, 512, 1, stride=1, padding=0)
        self.conv1 = torch.nn.Conv2d(512, 1024, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(1024, 512, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(512, 512, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(512, 512, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(512, 512, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(512, 512, 1, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(512, 1024, 1, stride=1, padding=0)
        self.conv8 = torch.nn.Conv2d(1024, 1024, 1, stride=1, padding=0)
        self.conv9 = torch.nn.Conv2d(1024, 512, 1, stride=1, padding=0)
        self.conv10 = torch.nn.Conv2d(512, 256, 1, stride=1, padding=0)
        self.conv11 = torch.nn.Conv2d(256, 256, 1, stride=1, padding=0)
        self.conv12 = torch.nn.Conv2d(256, 256, 1, stride=1, padding=0)
        self.conv13 = torch.nn.Conv2d(256, 256, 1, stride=1, padding=0)
        self.conv14 = torch.nn.Conv2d(256, 256, 3, stride=1, padding=1)
        self.conv15 = torch.nn.Conv2d(256, 128, 3, stride=1, padding=1)
        self.conv16 = torch.nn.Conv2d(128, 6, 3, stride=1, padding=1)
        self.softmax = torch.nn.Softmax(dim=1)
        self.relu = torch.nn.ReLU(inplace=True)
        self.bn0 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1)
        self.bn1 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1)
        self.bn2 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1)
        self.bn3 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1)
        self.bn4 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1)
        self.bn5 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1)
        self.bn6 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1)
        self.bn7 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1)
        self.bn8 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1)
        self.bn9 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1)
        self.bn10 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1)
        self.bn11 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1)
        self.bn12 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1)
        self.bn13 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1)
        self.bn14 = torch.nn.BatchNorm2d(128, eps=1e-05, momentum=0.1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv0(x1)
        v1 = self.relu(v1)
        v1 = self.bn0(v1)
        v1 = self.conv1(v1)
        v1 = self.relu(v1)
        v1 = self.bn1(v1)
        v1 = self.conv2(v1)
        v1 = self.relu(v1)
        v1 = self.bn2(v1)
        v1 = self.conv3(v1)
        v1 = self.relu(v1)
        v1 = self.bn3(v1)
        v1 = self.conv4(v1)
        v1 = self.relu(v1)
        v1 = self.bn4(v1)
        v1 = self.conv5(v1)
        v1 = self.relu(v1)
        v1 = self.bn5(v1)
        v1 = self.conv6(v1)
        v1 = self.relu(v1)
        v1 = self.bn6(v1)
        v1 = self.conv7(v1)
        v1 = self.relu(v1)
        v1 = self.bn7(v1)
        v1 = self.conv8(v1)
        v1 = self.relu(v1)
        v1 = self.bn8(v1)
        v1 = self.conv9(v1)
        v1 = self.relu(v1)
        v1 = self.bn9(v1)
        v1 = self.conv10(v1)
        v1 = self.relu(v1)
        v1 = self.bn10(v1)
        return v1
    x1 = torch.randn(1, 512, 14, 14)
    x2 = torch.randn(1, 1024, 14, 14)
    x3 = torch.randn(1, 1024, 14, 14)
    x4 = torch.randn(1, 512, 14, 14)
    x5 = torch.randn(1, 512, 7, 7)
    x6 = torch.randn(1, 1024, 7, 7)
    x7 = torch.randn(1, 256, 56, 56)
    x8 = torch.randn(1, 256, 56, 56)
    x9 = torch.randn(1, 128, 56, 56)


min_value = 1

func = Model(min_value).to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (int, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, !int!)
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, !int!)


jit:
conv2d() received an invalid combination of arguments - got (int, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, !int!)
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, !int!)

'''