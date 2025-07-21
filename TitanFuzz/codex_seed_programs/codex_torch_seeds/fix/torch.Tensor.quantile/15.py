'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 4)
torch.Tensor.quantile(input_tensor, 0.5, dim=None, keepdim=False)
torch.Tensor.quantile(input_tensor, 0.5, dim=0, keepdim=False)
torch.Tensor.quantile(input_tensor, 0.5, dim=1, keepdim=False)
torch.Tensor.quantile(input_tensor, 0.5, dim=None, keepdim=True)
torch.Tensor.quantile(input_tensor, 0.5, dim=0, keepdim=True)
torch.Tensor.quantile(input_tensor, 0.5, dim=1, keepdim=True)