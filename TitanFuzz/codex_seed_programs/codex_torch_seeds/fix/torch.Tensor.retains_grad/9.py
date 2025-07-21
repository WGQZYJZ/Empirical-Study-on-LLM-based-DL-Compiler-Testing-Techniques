'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retains_grad\ntorch.Tensor.retains_grad(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(3, 3)
torch.Tensor.retains_grad(_input_tensor, True)
print(_input_tensor)