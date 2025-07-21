'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(torch.flatten(x))
print(torch.flatten(x, start_dim=1))
print(torch.flatten(x, end_dim=1))