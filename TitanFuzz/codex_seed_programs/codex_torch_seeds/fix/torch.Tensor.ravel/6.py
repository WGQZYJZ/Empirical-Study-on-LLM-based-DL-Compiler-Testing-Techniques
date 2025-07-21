'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
output_tensor = input_tensor.ravel()
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape\ntorch.Tensor.reshape(input, shape)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
output_tensor = input_tensor.reshape(2, 6)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(input, dim=None)\n'
import torch
input_tensor = torch.randn(3, 1, 4, 1)
print(input_tensor)
output_tensor = input_tensor.squeeze()