'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_storage\ntorch.is_storage(obj)\n'
import torch
data = torch.randn(1, 2, 3)
print(torch.is_storage(data))