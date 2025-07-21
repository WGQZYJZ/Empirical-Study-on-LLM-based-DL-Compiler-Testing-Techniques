'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.transpose(input, 0, 1)
print(input)
print(output)