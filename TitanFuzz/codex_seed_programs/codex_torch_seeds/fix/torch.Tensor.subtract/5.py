'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
result = torch.Tensor.subtract(input_tensor, other_tensor)
print(result)
result = torch.Tensor.subtract(input_tensor, other_tensor, alpha=0.5)
print(result)