'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_shapes\ntorch.broadcast_shapes(*shapes)\n'
import torch
x = torch.tensor([1, 2, 3])
y = torch.tensor([1, 2, 3])
z = torch.tensor([1, 2, 3])
print(torch.broadcast_shapes(x.shape, y.shape, z.shape))