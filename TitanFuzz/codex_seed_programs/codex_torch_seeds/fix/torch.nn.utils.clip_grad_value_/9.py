'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
import torch
x = torch.arange((- 10), 10, dtype=torch.float32)
y = torch.arange((- 10), 10, dtype=torch.float32)
torch.nn.utils.clip_grad_value_(x, clip_value=1.0)
print(x)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_norm_\ntorch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2)\n'
import torch
import torch
x = torch.arange((- 10), 10, dtype=torch.float32)
y = torch.arange((- 10), 10, dtype=torch.float32)
torch.nn.utils.clip_grad_norm_(x, max_norm=1.0, norm_type=2)
print