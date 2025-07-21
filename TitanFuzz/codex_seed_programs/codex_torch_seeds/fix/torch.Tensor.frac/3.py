'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac\ntorch.Tensor.frac(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
fractional_part = torch.Tensor.frac(input_tensor)
print(fractional_part)