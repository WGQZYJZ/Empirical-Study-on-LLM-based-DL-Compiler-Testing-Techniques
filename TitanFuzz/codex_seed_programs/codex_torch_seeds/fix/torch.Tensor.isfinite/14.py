'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isfinite\ntorch.Tensor.isfinite(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(10, 10)
print(input_tensor.isfinite())
print(input_tensor.isinf())
print(input_tensor.isnan())
print(torch.isfinite(input_tensor))
print(torch.isinf(input_tensor))
print(torch.isnan(input_tensor))