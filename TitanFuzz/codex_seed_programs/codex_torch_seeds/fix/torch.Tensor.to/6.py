'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to\ntorch.Tensor.to(_input_tensor, *args, **kwargs)\n'
import torch
input_tensor = torch.randn(3, 3)
torch.Tensor.to(input_tensor, torch.device('cuda:0'))