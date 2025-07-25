import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        yuzu.onnxrt.set_training(1) # set training on
        v2 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v3 = v2.permute(0, 2, 1)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(4, 2, 2)
