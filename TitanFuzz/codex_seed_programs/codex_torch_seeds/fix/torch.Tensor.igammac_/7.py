'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igammac_\ntorch.Tensor.igammac_(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(2, 3, dtype=torch.float64)
other = torch.randn(2, 3, dtype=torch.float64)
result = torch.Tensor.igammac_(_input_tensor, other)
print(result)