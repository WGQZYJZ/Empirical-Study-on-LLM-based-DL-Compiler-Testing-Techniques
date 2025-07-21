'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(torch.unbind(x, dim=0))
print(torch.unbind(x, dim=1))