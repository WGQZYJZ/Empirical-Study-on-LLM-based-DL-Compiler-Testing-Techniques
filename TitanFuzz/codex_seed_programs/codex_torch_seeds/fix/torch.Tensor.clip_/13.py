'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip_\ntorch.Tensor.clip_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
torch.Tensor.clip_(input_tensor, min=0.4, max=0.6)
print(input_tensor)