'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(torch.isposinf(input))