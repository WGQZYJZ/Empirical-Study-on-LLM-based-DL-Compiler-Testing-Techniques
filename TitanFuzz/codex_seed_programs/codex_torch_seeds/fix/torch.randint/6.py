'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint\ntorch.randint(low=0, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
data_size = 5
data_low = 0
data_high = 10
output = torch.randint(low=data_low, high=data_high, size=(data_size,), dtype=torch.float32)
print('output = \n', output)