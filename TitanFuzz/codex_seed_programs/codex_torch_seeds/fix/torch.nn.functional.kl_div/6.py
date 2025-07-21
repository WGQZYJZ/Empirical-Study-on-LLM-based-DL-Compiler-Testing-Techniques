"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.kl_div\ntorch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import torch.nn.functional as F
import torch
x = torch.tensor([[0, 1, 2], [1, 2, 3]])
y = torch.tensor([[0, 1, 2], [1, 2, 3]])
loss = F.kl_div(x, y, reduction='none')
print(loss)
loss = F.kl_div(x, y, reduction='sum')
print(loss)
loss = F.kl_div(x, y, reduction='mean')
print(loss)
loss = F.kl_div(x, y, reduction='batchmean')
print(loss)