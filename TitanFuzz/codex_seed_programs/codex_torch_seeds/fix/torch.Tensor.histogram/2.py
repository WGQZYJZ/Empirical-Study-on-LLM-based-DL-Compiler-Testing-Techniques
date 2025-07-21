'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
input_tensor = torch.randint(0, 10, (200,), dtype=torch.float)
hist_tensor = input_tensor.histogram(bins=10, range=(0, 10))
print(hist_tensor)