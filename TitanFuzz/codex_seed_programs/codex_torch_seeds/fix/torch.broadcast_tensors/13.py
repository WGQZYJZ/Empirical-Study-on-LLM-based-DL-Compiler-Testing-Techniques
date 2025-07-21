'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6]])
z = torch.broadcast_tensors(x, y)
print(z)