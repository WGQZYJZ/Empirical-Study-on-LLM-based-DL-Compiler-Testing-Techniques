"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gaussian_nll_loss\ntorch.nn.functional.gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean')\n"
import torch
input = torch.Tensor([[1, 2, 3], [4, 5, 6]])
target = torch.Tensor([[1, 2, 3], [4, 5, 6]])
var = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output = torch.nn.functional.gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean')
print(output)