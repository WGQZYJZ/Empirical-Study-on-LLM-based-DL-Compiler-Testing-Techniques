'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
sum_to_size_result = torch.Tensor.sum_to_size(input_tensor, 3, 4)
print('sum_to_size_result: ', sum_to_size_result)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size, out=None)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
sum_to_size_result = torch.Tensor.sum_to_size(input_tensor, 3, 4, out=None)