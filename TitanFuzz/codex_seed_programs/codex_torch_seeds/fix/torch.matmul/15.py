'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
other_data = torch.randn(3, 2)
output_data = torch.matmul(input_data, other_data)
print(input_data)
print(other_data)
print(output_data)