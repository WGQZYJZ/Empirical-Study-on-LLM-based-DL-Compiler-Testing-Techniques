'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.are_deterministic_algorithms_enabled\ntorch.are_deterministic_algorithms_enabled()\n'
import torch
x = torch.randn(5, 5, dtype=torch.float64)
y = torch.randn(5, 5, dtype=torch.float64)
torch.are_deterministic_algorithms_enabled()