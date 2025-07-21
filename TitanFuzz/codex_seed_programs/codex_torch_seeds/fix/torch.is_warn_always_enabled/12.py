'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_warn_always_enabled\ntorch.is_warn_always_enabled()\n'
import torch
input_data = torch.tensor([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
print(torch.is_warn_always_enabled())