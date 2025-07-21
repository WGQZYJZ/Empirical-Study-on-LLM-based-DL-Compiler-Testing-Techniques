'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
x = torch.randn(3, 4)
print(x)
indices = torch.tensor([0, 2])
y = torch.take(x, indices)
print(y)