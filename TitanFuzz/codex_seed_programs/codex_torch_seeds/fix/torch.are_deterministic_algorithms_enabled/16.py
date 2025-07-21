'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.are_deterministic_algorithms_enabled\ntorch.are_deterministic_algorithms_enabled()\n'
import torch
x = torch.randn(1, 1, requires_grad=True, dtype=torch.float32)
y = torch.randn(1, 1, requires_grad=True, dtype=torch.float32)
z = (x * y)
print(z)
torch.are_deterministic_algorithms_enabled()