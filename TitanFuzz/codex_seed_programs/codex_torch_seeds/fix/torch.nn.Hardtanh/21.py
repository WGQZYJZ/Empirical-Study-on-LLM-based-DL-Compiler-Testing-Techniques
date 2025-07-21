'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
import numpy as np
import torch
x = torch.tensor(np.array([(- 2.0), (- 1.0), 0.0, 1.0, 2.0, 3.0]))
print(x)
y = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)(x)
print(y)