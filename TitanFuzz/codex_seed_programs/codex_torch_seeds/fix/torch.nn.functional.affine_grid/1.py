'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.affine_grid\ntorch.nn.functional.affine_grid(theta, size, align_corners=None)\n'
import torch
import torch.nn.functional as F
dtype = torch.float
device = torch.device('cpu')
(batch_size, input_channels, input_height, input_width) = (4, 1, 5, 5)
theta = torch.randn(batch_size, 2, 3, device=device, dtype=dtype)
size = torch.Size((batch_size, input_channels, input_height, input_width))
grid = F.affine_grid(theta, size)
print(grid.size())
'\nOutput:\ntorch.Size([4, 1, 5, 5, 2])\n'