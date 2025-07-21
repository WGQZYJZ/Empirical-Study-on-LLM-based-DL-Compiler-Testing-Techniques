'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
input = torch.randn(1, 2, 3, 4)
print(input)
output = torch.reshape(input, (2, 3, 4))
print(output)