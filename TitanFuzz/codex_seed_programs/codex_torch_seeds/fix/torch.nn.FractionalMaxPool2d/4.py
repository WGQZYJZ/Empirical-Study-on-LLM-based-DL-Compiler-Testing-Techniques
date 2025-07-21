'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool2d\ntorch.nn.FractionalMaxPool2d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch
input = torch.randn(20, 16, 50, 32)
torch.nn.FractionalMaxPool2d(3, output_size=13, _random_samples=None)