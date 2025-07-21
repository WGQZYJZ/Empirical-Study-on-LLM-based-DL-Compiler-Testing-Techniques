'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isclose\ntorch.Tensor.isclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
import torch
input_tensor = torch.rand(4, 4)
other_tensor = torch.rand(4, 4)
torch.Tensor.isclose(input_tensor, other_tensor, rtol=1e-05, atol=1e-08, equal_nan=False)
print(torch.Tensor.isclose(input_tensor, other_tensor, rtol=1e-05, atol=1e-08, equal_nan=False))