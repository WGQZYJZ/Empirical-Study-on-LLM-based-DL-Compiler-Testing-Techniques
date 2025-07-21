'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import torch
data = torch.randn(2, 3)
print(data)
torch.set_warn_always(True)
data.add(1)
print(data)