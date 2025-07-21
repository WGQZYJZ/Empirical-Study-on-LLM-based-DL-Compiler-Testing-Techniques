'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
x = torch.rand(2, 3, dtype=torch.float32)
print(x)
torch.use_deterministic_algorithms(True)
torch.use_deterministic_algorithms(False)