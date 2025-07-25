import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_19 = torch.nn.ConvTranspose2d(266, 728, 1, stride=2, padding=0)
        self.conv_transpose_31 = torch.nn.ConvTranspose3d(728, 1024, 1, stride=1, padding=0)
        self.conv_transpose_26 = torch.nn.ConvTranspose3d(384, 384, 1, stride=1, padding=0)
        self.maxpool3d_1 = torch.nn.MaxPool3d(kernel_size=[2, 2, 2], stride=2, padding=1, dilation=2)
        self.avgpool3d_0 = torch.nn.AvgPool3d(kernel_size=[2, 2, 2], stride=2, padding=0)
        self.conv_transpose_21 = torch.nn.ConvTranspose2d(384, 448, 1, stride=1, padding=0)
        self.maxpool2d_1 = torch.nn.MaxPool2d(kernel_size=[2, 2], stride=2)
        self.conv_transpose_24 = torch.nn.ConvTranspose2d(448, 256, 1, stride=1, padding=0)
        self.sigmoid_1 = torch.nn.Sigmoid()
        self.dropout_8 = torch.nn.Dropout3d()
        self.dropout_10 = torch.nn.Dropout2d()
        self.dropout_11 = torch.nn.Dropout2d()
        self.maxpool2d_2 = torch.nn.MaxPool2d(kernel_size=[2, 2], stride=2, padding=1)
        self.adaptive_avg_pool2d_1 = torch.nn.AdaptiveAvgPool2d((1, 1))
    def forward(self, x1):
        v1 = self.conv_transpose_19(x1)
        v2 = self.conv_transpose_31(v1)
        v3 = v2.size()
        v4 = torch.tanh(v3)
        v5 = self.conv_transpose_26(v4)
        v6 = self.maxpool3d_1(v5)
        v7 = self.avgpool3d_0(v6)
        v8 = self.conv_transpose_21(v7)
        v9 = torch.relu(v8)
        v10 = self.maxpool2d_1(v9)
        v11 = self.conv_transpose_24(v10)
        v12 = torch.tanh(v11)
        v13 = self.sigmoid_1(v12)
        v14 = self.dropout_8(v13, training=self.training)
        v15 = self.dropout_10(v14, training=self.training)
        v16 = self.dropout_11(v15, training=self.training)
        v17 = self.maxpool2d_2(v16)
        v18 = self.adaptive_avg_pool2d_1(v17)
        return v18
m = Model()
# Inputs to the model
x1 = torch.randn(1, 266, 29, 57, 29)
