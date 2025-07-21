'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.sigmoid\ntorch.nn.functional.sigmoid(input)\n'
import torch
input = torch.randn(1, 1)
print(input)
output = torch.nn.functional.sigmoid(input)
print(output)