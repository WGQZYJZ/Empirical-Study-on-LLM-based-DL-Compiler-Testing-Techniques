import torch
input = torch.randn(3, 4)
input
torch.quantile(input, 0.5, dim=1)
torch.quantile(input, 0.5, dim=1, keepdim=True)
torch.quantile(input, 0.5, dim=1, keepdim=True, out=torch.randn(3, 1))
torch.quantile(input, torch.tensor([0.5, 0.9]), dim=1)
torch.quantile(input, torch.tensor([0.5, 0.9]), dim=1, keepdim=True)