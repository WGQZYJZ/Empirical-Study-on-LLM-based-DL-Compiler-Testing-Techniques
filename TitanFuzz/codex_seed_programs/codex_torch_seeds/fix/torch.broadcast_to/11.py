'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
x = torch.tensor([1, 2, 3])
y = torch.broadcast_to(x, (3, 3))
print(y)