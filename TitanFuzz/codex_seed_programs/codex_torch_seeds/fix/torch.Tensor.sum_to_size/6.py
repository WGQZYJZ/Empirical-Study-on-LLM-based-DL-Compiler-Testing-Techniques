'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
import torch
input_tensor = torch.randn(3, 4, 5)
print(input_tensor.sum_to_size(4, 5))
print(input_tensor.sum_to_size(3, 5))