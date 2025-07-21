'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
torch.use_deterministic_algorithms(mode=True)
z = (x + y)
print(z)