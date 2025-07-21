'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
(min_value, min_idx) = torch.min(x, dim=1)
print('min_value: ', min_value)
print('min_idx: ', min_idx)
(min_value, min_idx) = torch.min(x, dim=0)
print('min_value: ', min_value)
print('min_idx: ', min_idx)
(min_value, min_idx) = torch.min(x, dim=1, keepdim=True)
print('min_value: ', min_value)
print('min_idx: ', min_idx)
(min_value, min_idx) = torch.min(x, dim=0, keepdim=True)