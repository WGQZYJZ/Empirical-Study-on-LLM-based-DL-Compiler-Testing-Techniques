'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_power\ntorch.matrix_power(input, n, *, out=None)\n'
import torch
input_data = torch.rand(3, 3)
print(input_data)
output_data = torch.matrix_power(input_data, 3)
print(output_data)