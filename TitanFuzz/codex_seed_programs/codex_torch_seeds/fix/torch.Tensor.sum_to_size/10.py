'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
print(torch.Tensor.sum_to_size(input_tensor, 1, 1))
print(torch.Tensor.sum_to_size(input_tensor, 2, 1))
print(torch.Tensor.sum_to_size(input_tensor, 1, 2))
print(torch.Tensor.sum_to_size(input_tensor, 2, 2))
print(torch.Tensor.sum_to_size(input_tensor, 2, 3))
print(torch.Tensor.sum_to_size(input_tensor, 3, 3))
print(torch.Tensor.sum_to_size(input_tensor, 3, 2))
print(torch.Tensor.sum_to_size(input_tensor, 3, 1))