'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.scatter\ntorch.scatter(input, dim, index, src)\n'
import torch
input = torch.randn(3, 5)
print(input)
torch.scatter(input, 1, torch.tensor([[4, 1, 2], [3, 0, 0]]), 0.5)