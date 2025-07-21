'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
result = torch.Tensor.sub(input_tensor, other)
print(result)