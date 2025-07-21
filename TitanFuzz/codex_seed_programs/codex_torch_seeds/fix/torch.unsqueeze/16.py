'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
x = torch.tensor([1, 2, 3, 4])
y = torch.unsqueeze(x, 0)
print(y)
y = torch.unsqueeze(x, 1)
print(y)