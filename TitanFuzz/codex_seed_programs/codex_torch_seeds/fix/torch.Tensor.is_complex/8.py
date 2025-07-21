'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor)\n'
import torch
input_tensor = torch.randn(10, device='cpu')
print(input_tensor.is_complex())
input_tensor = torch.randn(10, device='cpu', dtype=torch.complex64)
print(input_tensor.is_complex())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
input_tensor = torch.randn(10, device='cpu')
print(input_tensor.is_floating_point())
input_tensor = torch.randn(10, device='cpu', dtype=torch.complex64)
print(input_tensor.is_floating_point())