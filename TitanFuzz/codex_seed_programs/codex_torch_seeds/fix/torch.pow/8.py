'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
data = torch.tensor([[1, 2], [3, 4]])
result = torch.pow(data, 2)
print(result)