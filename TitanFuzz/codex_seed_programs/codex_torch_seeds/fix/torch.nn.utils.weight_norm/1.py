"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
from torch.nn import Conv1d, Conv2d, Conv3d, Linear, Embedding, Parameter
from torch.nn.utils import weight_norm
import torch
input = torch.randn(2, 3, 4, 5)
weight_norm(Conv2d(3, 4, kernel_size=3), name='weight')
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.spectral_norm\ntorch.nn.utils.spectral_norm(module, name='weight', n_power_iterations=1, dim=0, eps=1e-12, dtype=None)\n"
import torch
from torch.nn import Conv1d, Conv2d, Conv3d, Linear, Embedding, Parameter
from torch.nn.utils import spectral_norm