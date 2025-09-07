import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        # Use onnx torch.sigmoid to generate the module
        v1 = sigmoid(x1)
        pass
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 112, 112)
