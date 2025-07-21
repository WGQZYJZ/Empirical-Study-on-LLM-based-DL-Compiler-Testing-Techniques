'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.can_cast\ntorch.can_cast(from, to)\n'
import torch
x = torch.tensor([1, 2, 3, 4])
print(torch.can_cast(x.dtype, torch.float))