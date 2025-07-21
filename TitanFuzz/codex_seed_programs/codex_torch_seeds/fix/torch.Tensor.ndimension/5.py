'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor.ndimension())
input_tensor = torch.randn(2, 3, 4)
print(input_tensor.ndimension())
input_tensor = torch.randn(2, 3, 4, 5)
print(input_tensor.ndimension())
input_tensor = torch.randn(2, 3, 4, 5, 6)
print(input_tensor.ndimension())