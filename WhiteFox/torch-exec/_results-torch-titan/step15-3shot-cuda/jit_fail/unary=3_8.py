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

    def __init__(self, num_classes=1000):
        super(Model, self).__init__()
        self.features = nn.Sequential(nn.Conv2d(3, 32, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(32, 32, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1), nn.ReLU(inplace=True), nn.Conv2d(64, 64, kernel_size=3, stride=2, padding=1), nn.ReLU(inplace=True), nn.Conv2d(64, 128, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(128, 128, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(128, 128, kernel_size=3, stride=2, padding=1), nn.ReLU(inplace=True), nn.Conv2d(128, 256, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(256, 256, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(256, 256, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(256, 256, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(256, 256, kernel_size=3, stride=2, padding=1), nn.ReLU(inplace=True), nn.Conv2d(256, 256, kernel_size=3, stride=2, padding=1), nn.ReLU(inplace=True), nn.Conv2d(256, 512, kernel_size=3, padding=1, dilation=1), nn.ReLU(inplace=True), nn.Conv2d(512, 512, kernel_size=3, padding=1, dilation=1), nn.ReLU(inplace=True), nn.Conv2d(512, 512, kernel_size=3, padding=1, dilation=1), nn.ReLU(inplace=True), nn.Conv2d(512, 512, kernel_size=3, padding=1, dilation=1), nn.ReLU(inplace=True), nn.Conv2d(512, 512, kernel_size=3, padding=1, dilation=1), nn.ReLU(inplace=True), nn.Conv2d(512, 512, kernel_size=3, padding=1, dilation=1), nn.ReLU(inplace=True), nn.Conv2d(512, 1024, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(1024, 1024, kernel_size=3, padding=1), nn.ReLU(inplace=True))
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(in_features=1024, out_features=num_classes)

    def forward(self, x1, x2):
        x = self.features(x1)
        if (x2 is not None):
            x = torch.cat([x, x2], dim=1)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)



x2 = torch.randn(1, 1024, 1, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 14 but got size 1 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x729bbc6699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 1024, 14, 14)), FakeTensor(..., device='cuda:0', size=(1, 1024, 1, 1))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 14 but got 1 for tensor number 1 in the list

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''