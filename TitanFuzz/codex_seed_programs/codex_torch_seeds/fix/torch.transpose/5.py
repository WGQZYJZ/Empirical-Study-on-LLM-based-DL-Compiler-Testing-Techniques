'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x)
y = torch.transpose(x, 0, 1)
print(y)