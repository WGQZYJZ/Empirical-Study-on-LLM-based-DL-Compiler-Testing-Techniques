'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor.is_complex())
input_tensor = torch.rand(2, 3, dtype=torch.complex64)
print(input_tensor.is_complex())
input_tensor = torch.rand(2, 3, dtype=torch.complex128)
print(input_tensor.is_complex())