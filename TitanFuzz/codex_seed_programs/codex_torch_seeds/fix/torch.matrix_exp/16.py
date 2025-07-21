'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_exp\ntorch.matrix_exp(input)\n'
import torch
input_data = torch.rand(2, 2)
print(input_data)
output = torch.matrix_exp(input_data)
print(output)