import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        block_0 = [torch.nn.Conv2d(3, 32, 3, 1, 0, bias=False), torch.nn.ReLU(), torch.nn.Conv2d(32, 32, 3, 1, 1, bias=False), torch.nn.ReLU(), torch.nn.BatchNorm2d(32)]
        block_1 = [torch.nn.ReLU(), torch.nn.Conv2d(32, 32, 3, 1, 0, bias=False), torch.nn.ReLU(), torch.nn.BatchNorm2d(32)]
        block_2 = [torch.nn.ReLU(), torch.nn.Conv2d(32, 64, 3, 1, 0, bias=False), torch.nn.BatchNorm2d(64)]
        block_3 = []
        self.features = torch.nn.Sequential(*block_0, *block_1, *block_2, *block_3)
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
