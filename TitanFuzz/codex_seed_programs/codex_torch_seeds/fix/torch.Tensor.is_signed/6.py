'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_signed\ntorch.Tensor.is_signed(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 4, 5)
is_signed = input_tensor.is_signed()
print(is_signed)