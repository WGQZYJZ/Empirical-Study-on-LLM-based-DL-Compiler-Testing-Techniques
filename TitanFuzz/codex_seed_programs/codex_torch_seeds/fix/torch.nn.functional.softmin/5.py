'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softmin\ntorch.nn.functional.softmin(input, dim=None, _stacklevel=3, dtype=None)\n'
import torch
x = torch.tensor([[1, 2, 3, 4], [2, 3, 4, 5]], dtype=torch.float32)
print(x)
print(torch.nn.functional.softmin(x, dim=1))
print(torch.nn.functional.softmin(x, dim=0))