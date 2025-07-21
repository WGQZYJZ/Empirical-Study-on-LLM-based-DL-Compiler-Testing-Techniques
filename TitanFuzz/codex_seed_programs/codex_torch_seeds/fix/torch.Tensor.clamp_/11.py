'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp_\ntorch.Tensor.clamp_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.rand(4, 4)
print(input_tensor)
torch.Tensor.clamp_(input_tensor, min=0.0, max=1.0)
print(input_tensor)