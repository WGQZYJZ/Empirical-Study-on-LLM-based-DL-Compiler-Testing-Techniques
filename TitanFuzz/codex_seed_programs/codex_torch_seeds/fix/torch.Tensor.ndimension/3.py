'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(f'The dimension of input tensor is {input_tensor.ndimension()}')
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numel\ntorch.Tensor.numel(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(f'The number of elements in input tensor is {input_tensor.numel()}')