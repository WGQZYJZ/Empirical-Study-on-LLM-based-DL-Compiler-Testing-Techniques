'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x)
print(torch.ravel(x))