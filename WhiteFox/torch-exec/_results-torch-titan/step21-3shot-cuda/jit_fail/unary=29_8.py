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

    def __init__(self, min_value=0.3, max_value=12):
        super().__init__()
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(16, 8, 1, stride=1, padding=0, output_padding=1)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(16, 8, 1, stride=1, padding=0)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(16, 8, 1, stride=1, padding=0, output_padding=1)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(16, 8, 1, stride=1, padding=0)
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(16, 8, 1, stride=1, padding=0, output_padding=1)
        self.conv_transpose_6 = torch.nn.ConvTranspose2d(16, 8, 1, stride=1, padding=0, output_padding=2)
        self.conv_transpose_7 = torch.nn.ConvTranspose2d(16, 8, 2, stride=3, padding=1, dilation=1, output_padding=1)
        self.conv_transpose_8 = torch.nn.ConvTranspose2d(16, 8, 3, stride=2, padding=0, output_padding=1)
        self.conv_transpose_9 = torch.nn.ConvTranspose2d(16, 8, 3, stride=1, padding=0)
        self.conv_transpose_10 = torch.nn.ConvTranspose2d(16, 8, 3, stride=4, padding=0, dilation=2, output_padding=1)
        self.conv_transpose_11 = torch.nn.ConvTranspose2d(16, 8, 3, stride=4, padding=0, dilation=1, output_padding=2)
        self.conv_transpose_12 = torch.nn.ConvTranspose2d(16, 8, 3, stride=3, padding=0, dilation=1, output_padding=3)
        self.conv_transpose_13 = torch.nn.ConvTranspose2d(16, 8, 3, stride=2, padding=0, output_padding=3)
        self.conv_transpose_14 = torch.nn.ConvTranspose2d(16, 8, 4, stride=2, padding=0, output_padding=1)
        self.conv_transpose_15 = torch.nn.ConvTranspose2d(16, 8, 4, stride=1, padding=0, dilation=2, output_padding=1)
        self.conv_transpose_16 = torch.nn.ConvTranspose2d(16, 8, 5, stride=1, padding=0, output_padding=0)
        self.conv_transpose_17 = torch.nn.ConvTranspose2d(16, 8, 2, stride=2, padding=1, output_padding=1)
        self.conv_transpose_18 = torch.nn.ConvTranspose2d(16, 8, 3, stride=4, padding=1, dilation=2, output_padding=1)
        self.conv_transpose_19 = torch.nn.ConvTranspose2d(16, 8, 3, stride=3, padding=2, dilation=3, output_padding=3)
        self.conv_transpose_20 = torch.nn.ConvTranspose2d(16, 8, 3, stride=1, padding=1, dilation=3, output_padding=3)
        self.conv_transpose_21 = torch.nn.ConvTranspose2d(16, 16, 1, stride=1, padding=0, output_padding=7)
        self.conv_transpose_22 = torch.nn.ConvTranspose2d(16, 32, 1, stride=1, padding=0, output_padding=0)
        self.conv_transpose_23 = torch.nn.ConvTranspose2d(32, 64, 2, stride=2, padding=0, output_padding=0)
        self.conv_transpose_24 = torch.nn.ConvTranspose2d(64, 16, 3, stride=3, padding=2, dilation=3, output_padding=0)
        self.conv_transpose_25 = torch.nn.ConvTranspose2d(64, 2, 3, stride=3, padding=3)
        self.conv_transpose_26 = torch.nn.ConvTranspose2d(64, 16, 3, stride=2, padding=0, output_padding=1)
        self.conv_transpose_27 = torch.nn.ConvTranspose2d(64, 16, 2, stride=2, padding=0, output_padding=0)
        self.conv_transpose_28 = torch.nn.ConvTranspose2d(64, 16, 1, stride=1, padding=0, output_padding=2)
        self.conv_transpose_29 = torch.nn.ConvTranspose2d(64, 8, 2, stride=2, padding=0, output_padding=1)
        self.conv_transpose_30 = torch.nn.ConvTranspose2d(64, 8, 3, stride=1, padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1, x2):
        v1 = self.conv_transpose_1(x1)
        h1 = torch.transpose(v1, 1, 2)
        h2 = torch.transpose(v1, 2, 3)
        g1 = torch.cat(tensors=[h1, h2], dim=1)
        g2 = self.conv_transpose_2(g1)
        g3 = torch.transpose(g2, 1, 2)
        h3 = torch.transpose(g3, 3, 4)
        g4 = self.conv_transpose_3(h3)
        g5 = torch.swapaxes(g4, 1, 4)
        g6 = torch.swapaxes(g4, 1, 3)
        g7 = torch.transpose(g6, 1, 2)
        g8 = self.conv_transpose_4(g7)
        g9 = torch.transpose(g8, 1, 2)
        h4 = torch.transpose(g9, 3, 4)
        g10 = self.conv_transpose_5(h4)
        g11 = torch.swapaxes(g10, 1, 3)
        g12 = torch.swapaxes(g10, 1, 2)
        g13 = torch.transpose(g12, 1, 2)
        g14 = self.conv_transpose_6(g13)
        h5 = torch.transpose(g14, 3, 4)
        g15 = self.conv_transpose_7(h5)
        h6 = torch.transpose(g15, 3, 4)
        g16 = self.conv_transpose_8(h6)
        h7 = torch.transpose(g16, 3, 4)
        g17 = self.conv_transpose_9(h7)
        h8 = torch.transpose(g17, 3, 4)
        g18 = self.conv_transpose_10(h8)
        h9 = torch.transpose(g18, 3, 4)
        g19 = self.conv_transpose_11(h9)
        h10 = torch.transpose(g19, 3, 4)
        g20 = self.conv_transpose_12(h10)
        h11 = torch.transpose(g20, 3, 4)
        g21 = self.conv_transpose_13(h11)
        h12 = torch.transpose(g21, 3, 4)
        g22 = self.conv_transpose_14(h12)
        h13 = torch.transpose(g22, 3, 4)
        g23 = self.conv_transpose_15(h13)
        h14 = torch.transpose(g23, 3, 4)
        g24 = self.conv_transpose_16(h14)
        h15 = torch.transpose(g24, 3, 4)
        g25 = self.conv_transpose_17(h15)
        h16 = torch.transpose(g25, 3, 4)
        g26 = self.conv_transpose_18(h16)
        h17 = torch.transpose(g26, 3, 4)
        g27 = self.conv_transpose_19(h17)
        h18 = torch.transpose(g27, 3, 4)
        g28 = self.conv_transpose_20(h18)
        h19 = torch.transpose(g28, 3, 4)
        g29 = self.conv_transpose_21(h19)
        h20 = torch.transpose(g29, 3, 4)
        g30 = self.conv_transpose_22(h20)
        h21 = torch.transpose(g30, 3, 4)
        g31 = self.conv_transpose_23(h21)
        h24 = torch.relu(g31)
        g32 = torch.transpose(g31, 1, 2)
        g33 = self.conv_transpose_24(g32)
        h25 = torch.transpose(g33, 3, 4)
        g34 = self.conv_transpose_25(h25)
        h26 = torch.transpose(g34, 3, 4)
        g35 = self.conv_transpose_26(h26)
        h27 = torch.transpose(g35, 3, 4)
        g36 = self.conv_transpose_27(h27)
        h28 = torch.transpose(g36, 3, 4)
        g37 = self.conv_transpose_28(h28)
        h29 = torch.transpose(g37, 3, 4)
        g38 = self.conv_transpose_29(h29)
        h30 = torch.transpose(g38, 3, 4)
        g39 = self.conv_transpose_30(h30)
        v2 = torch.tanh(g39)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 16, 31, 31)



x2 = torch.randn(1, 64, 7, 7)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
Failed running call_function <built-in method cat of type object at 0x7daf096699e0>(*(), **{'tensors': [FakeTensor(..., device='cuda:0', size=(1, 32, 8, 32)), FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32))], 'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 8 but got 32 for tensor number 1 in the list

from user code:
   File "<string>", line 56, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''