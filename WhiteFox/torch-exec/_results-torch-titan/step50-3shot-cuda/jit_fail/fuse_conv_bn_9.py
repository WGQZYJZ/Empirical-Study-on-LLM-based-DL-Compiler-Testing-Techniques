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



class AlexNet(nn.Module):

    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(nn.Conv2d(3, 64, kernel_size=3, stride=2, padding=1), nn.ReLU(inplace=True), nn.Conv2d(64, 192, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.MaxPool2d(kernel_size=2, stride=2), nn.Conv2d(192, 384, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(384, 256, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(256, 256, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.MaxPool2d(kernel_size=2, stride=2))
        self.classifier = nn.Sequential(nn.Linear(((256 * 2) * 2), 4096), nn.ReLU(inplace=True), nn.Linear(4096, 4096), nn.ReLU(inplace=True), nn.Linear(4096, 10))

    def forward(self, x1):
        x = self.features(x1)
        x1 = x.view(x.size(0), ((256 * 2) * 2))
        x1 = self.classifier(x1)
        return x




func = AlexNet().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 1024]' is invalid for input of size 4096

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 256, 4, 4)), 1, 1024), **{}):
shape '[1, 1024]' is invalid for input of size 4096

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''