"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.kl_div\ntorch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import numpy as np
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
target = torch.tensor([[1, 2, 3], [4, 5, 6]])
loss = torch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)
print(loss)