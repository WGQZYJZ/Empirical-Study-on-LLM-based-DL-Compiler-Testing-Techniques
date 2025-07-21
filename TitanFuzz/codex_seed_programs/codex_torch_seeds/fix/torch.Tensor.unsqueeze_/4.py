'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze_\ntorch.Tensor.unsqueeze_(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
torch.Tensor.unsqueeze_(input_tensor, dim=0)
print(input_tensor)