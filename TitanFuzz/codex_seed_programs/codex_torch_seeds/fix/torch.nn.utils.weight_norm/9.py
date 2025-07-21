"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
from torch.nn import Linear, Conv2d, BatchNorm1d, BatchNorm2d, BatchNorm3d
from torch.nn.utils import weight_norm
import torch
linear = Linear(10, 10)
linear = weight_norm(linear)
conv = Conv2d(10, 10, kernel_size=3)
conv = weight_norm(conv)
bn = BatchNorm1d(10)
bn = weight_norm(bn)
bn = BatchNorm2d(10)
bn = weight_norm(bn)
bn = BatchNorm3d(10)
bn = weight_norm(bn)