'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(2, 3)
detach_output = torch.Tensor.detach(_input_tensor)
print(detach_output)