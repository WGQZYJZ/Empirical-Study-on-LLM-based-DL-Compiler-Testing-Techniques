'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
x = torch.rand(2, 2)
y = torch.rand(2, 2)
torch.use_deterministic_algorithms(mode=True)
z = (x + y)
print(z)
'\nTask 4: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
torch.use_deterministic_algorithms(mode=False)
z = (x + y)
print(z)