'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
input = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output = torch.narrow(input, 1, 1, 2)
print(output)