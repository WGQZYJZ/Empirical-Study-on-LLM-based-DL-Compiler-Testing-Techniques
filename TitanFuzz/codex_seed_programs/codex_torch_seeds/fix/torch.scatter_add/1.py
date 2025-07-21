'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.scatter_add\ntorch.scatter_add(input, dim, index, src)\n'
import torch
import torch
input = torch.randn(10, 10)
index = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
src = torch.randn(10, 1)
output = torch.scatter_add(input, 0, index.unsqueeze(1), src)
print(output)