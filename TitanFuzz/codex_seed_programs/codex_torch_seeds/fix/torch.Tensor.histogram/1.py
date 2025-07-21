'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
_input_tensor = torch.randint(low=0, high=100, size=(100,), dtype=torch.int)
hist = torch.Tensor.histogram(_input_tensor, bins=10)
print(hist)