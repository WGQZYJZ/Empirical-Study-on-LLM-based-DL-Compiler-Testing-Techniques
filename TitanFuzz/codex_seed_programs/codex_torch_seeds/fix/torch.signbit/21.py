'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
import torch
input_data = torch.randn(2, 2)
print(input_data)
output_data = torch.signbit(input_data)
print(output_data)