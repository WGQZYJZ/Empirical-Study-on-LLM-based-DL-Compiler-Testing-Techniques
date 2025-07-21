'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.real\ntorch.real(input)\n'
import torch
input = torch.randn(1, 2, 3, dtype=torch.float32)
print(input)
output = torch.real(input)
print(output)