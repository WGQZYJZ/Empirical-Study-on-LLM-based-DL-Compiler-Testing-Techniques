'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
x = torch.tensor([[(- 1.0), (- 0.5), 0.0, 0.5, 1.0]])
y = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)(x)
print(y)