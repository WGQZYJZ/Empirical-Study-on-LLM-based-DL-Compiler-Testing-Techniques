'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_exp\ntorch.matrix_exp(input)\n'
import torch
input = torch.rand(2, 2)
output = torch.matrix_exp(input)
print(output)