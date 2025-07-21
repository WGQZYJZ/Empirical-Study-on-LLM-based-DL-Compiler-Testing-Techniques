'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
x = torch.tensor([1, 2, 3])
print(torch.is_tensor(x))