'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor.ndimension())
input_tensor = torch.randn(3, 4, 5)
print(input_tensor.ndimension())
input_tensor = torch.randn(3, 4, 5, 6)
print(input_tensor.ndimension())
input_tensor = torch.randn(3, 4, 5, 6, 7)
print(input_tensor.ndimension())
input_tensor = torch.randn(3, 4, 5, 6, 7, 8)
print(input_tensor.ndimension())
input_tensor = torch.randn(3, 4, 5, 6, 7, 8, 9)
print(input_tensor.ndimension())