'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_exp\ntorch.matrix_exp(input)\n'
import torch
input_data = torch.randn(2, 2)
print(input_data)
print('\nTask 3: Call the API torch.matrix_exp')
print(torch.matrix_exp(input_data))