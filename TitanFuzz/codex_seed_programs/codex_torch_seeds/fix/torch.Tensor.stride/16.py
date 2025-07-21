'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
_input_tensor = torch.randn(2, 3, 4, 5)
print(torch.Tensor.stride(_input_tensor, dim=0))
print(torch.Tensor.stride(_input_tensor, dim=1))
print(torch.Tensor.stride(_input_tensor, dim=2))
print(torch.Tensor.stride(_input_tensor, dim=3))
'\nOutput:\n120\n40\n10\n2\n'