"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.kl_div\ntorch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import torch
input = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
target = torch.tensor([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
torch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)