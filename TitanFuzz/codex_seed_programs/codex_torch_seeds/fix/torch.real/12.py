'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.real\ntorch.real(input)\n'
import torch
input_data = torch.randn(2, 3)
output = torch.real(input_data)
print(output)