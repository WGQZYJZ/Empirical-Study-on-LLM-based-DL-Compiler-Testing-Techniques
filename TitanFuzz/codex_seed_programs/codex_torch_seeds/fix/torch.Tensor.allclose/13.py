'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.allclose\ntorch.Tensor.allclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
_input_tensor = torch.rand(10, 3)
other = torch.rand(10, 3)
print(torch.Tensor.allclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False))
print(torch.Tensor.allclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=True))
print(torch.Tensor.allclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=True))
print(torch.Tensor.allclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False))