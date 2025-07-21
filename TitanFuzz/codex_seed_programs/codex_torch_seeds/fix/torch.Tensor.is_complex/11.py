'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor)\n'
import torch
tensor_input = torch.randn(2, 3)
print(tensor_input.is_complex())
tensor_input = torch.randn(2, 3, dtype=torch.complex64)
print(tensor_input.is_complex())