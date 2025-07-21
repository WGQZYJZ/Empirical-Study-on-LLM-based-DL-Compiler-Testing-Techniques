'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
sum_tensor = torch.Tensor.sum_to_size(input_tensor, (1, 1))
print('The input tensor is: ', input_tensor)
print('The sum tensor is: ', sum_tensor)