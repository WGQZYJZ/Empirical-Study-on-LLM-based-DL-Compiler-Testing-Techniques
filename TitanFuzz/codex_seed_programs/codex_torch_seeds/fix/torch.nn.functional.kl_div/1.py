"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.kl_div\ntorch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import torch.nn.functional as F
import torch
input = torch.randn(2, 4)
target = torch.randn(2, 4)
output = F.kl_div(input, target, size_average=False, reduce=False)
print(output)
import torch
input = torch.randn(2, 4)
target = torch.randn(2, 4)
output = F.kl_div(input, target, size_average=True, reduce=False)
print(output)
import torch
input = torch.randn(2, 4)
target = torch.randn(2, 4)