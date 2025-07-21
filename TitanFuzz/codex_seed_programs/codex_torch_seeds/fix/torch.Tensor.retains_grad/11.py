'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retains_grad\ntorch.Tensor.retains_grad(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(1, requires_grad=True)
torch.Tensor.retains_grad(_input_tensor)