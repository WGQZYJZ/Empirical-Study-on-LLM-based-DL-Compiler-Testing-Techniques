'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxUnpool3d\ntorch.nn.MaxUnpool3d(kernel_size, stride=None, padding=0)\n'
import torch
x = torch.randn(2, 3, 4, 4, 4)
torch.nn.MaxUnpool3d(kernel_size=2, stride=2, padding=0)