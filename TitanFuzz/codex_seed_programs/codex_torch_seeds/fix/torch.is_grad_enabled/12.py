'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)
y = torch.tensor([1, 0, 1, 0, 1, 0, 1, 0, 1, 0], dtype=torch.float32)
print(torch.is_grad_enabled())