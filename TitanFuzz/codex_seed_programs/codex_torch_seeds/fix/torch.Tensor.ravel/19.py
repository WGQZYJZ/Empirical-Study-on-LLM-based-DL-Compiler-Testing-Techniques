'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
output_tensor = input_tensor.ravel()
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape\ntorch.Tensor.reshape(_input_tensor, _shape)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
output_tensor = input_tensor.reshape(3, 2)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, _dim)\n'
import torch