'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.can_cast\ntorch.can_cast(from, to)\n'
import torch
x = torch.tensor([1, 2, 3], dtype=torch.float32)
y = torch.tensor([1, 2, 3], dtype=torch.int32)
print(torch.can_cast(x.dtype, y.dtype))
print(torch.can_cast(y.dtype, x.dtype))