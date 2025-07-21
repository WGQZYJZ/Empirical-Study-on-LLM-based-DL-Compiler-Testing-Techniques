'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logcumsumexp\ntorch.logcumsumexp(input, dim, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
log_cumsum_exp_data = torch.logcumsumexp(input_data, dim=0)
print(log_cumsum_exp_data)
log_cumsum_exp_data = torch.logcumsumexp(input_data, dim=1)
print(log_cumsum_exp_data)