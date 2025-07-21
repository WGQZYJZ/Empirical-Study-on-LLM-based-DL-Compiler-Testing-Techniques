'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.real\ntorch.Tensor.real(_input_tensor, )\n'
import torch
input_data = torch.rand(1, 1, 2, 2)
real_data = input_data.real()
print(real_data)