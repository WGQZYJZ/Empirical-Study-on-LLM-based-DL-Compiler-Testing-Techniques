'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.t\ntorch.t(input)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.t(input)
print(output)