'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add_\ntorch.Tensor.add_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(4, 4)
other_tensor = torch.randn(4, 4)
torch.Tensor.add_(input_tensor, other_tensor)
print(input_tensor)