'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.geometric_\ntorch.Tensor.geometric_(_input_tensor, p, *, generator=None)\n'
import torch
input_tensor = torch.Tensor([0.2, 0.3, 0.4])
torch.Tensor.geometric_(input_tensor, p=0.5)
print(input_tensor)