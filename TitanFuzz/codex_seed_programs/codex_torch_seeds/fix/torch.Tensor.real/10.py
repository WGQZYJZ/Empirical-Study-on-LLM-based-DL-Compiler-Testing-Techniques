'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.real\ntorch.Tensor.real(_input_tensor, )\n'
import torch
input_data = torch.randn(10, 10)
output = input_data.real()
print(output)